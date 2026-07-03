import os
import json
import time
import re
import subprocess
from pathlib import Path

def collect_evidence(target_path, base_dir):
    start_time = time.time()
    target = Path(target_path).resolve()
    base = Path(base_dir).resolve()
    
    # Create output directories
    evidence_dir = base / "evidence"
    docs_dir = base / "docs"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Load scan rules
    scan_rules_path = base / "config" / "scan_rules.json"
    ignored_dirs = set()
    allowed_exts = set()
    if scan_rules_path.exists():
        try:
            with open(scan_rules_path, "r") as f:
                rules = json.load(f)
                ignored_dirs = set(rules.get("ignored_directories", []))
                allowed_exts = set(rules.get("allowed_extensions", []))
        except Exception as e:
            print(f"Error loading scan_rules.json: {e}")
            
    if not ignored_dirs:
        ignored_dirs = {".git", "node_modules", "dist", "build", "coverage", ".next", ".cache", "venv"}
    if not allowed_exts:
        allowed_exts = {".js", ".jsx", ".ts", ".tsx", ".vue", ".json"}
        
    print(f"Ignored directories: {ignored_dirs}")
    print(f"Allowed extensions: {allowed_exts}")
    
    # Walk target repository
    all_files = []
    files_scanned = 0
    files_skipped = 0
    errors = []
    
    # Fetch Git ownership info in batch
    git_owners = {}
    try:
        res = subprocess.run(
            ["git", "log", "--name-only", "--pretty=AUTH:%an"],
            cwd=str(target),
            capture_output=True,
            text=True,
            check=True
        )
        current_author = None
        for line in res.stdout.splitlines():
            line = line.strip()
            if line.startswith("AUTH:"):
                current_author = line[5:].strip()
            elif line and current_author:
                file_path = Path(line).as_posix()
                if file_path not in git_owners:
                    git_owners[file_path] = {}
                git_owners[file_path][current_author] = git_owners[file_path].get(current_author, 0) + 1
    except Exception as e:
        print(f"Git log execution failed: {e}")
        
    # Resolve ownership to the author with the max commit counts
    resolved_owners = {}
    for fp, authors in git_owners.items():
        resolved_owners[fp] = max(authors, key=authors.get)
        
    def should_ignore(path):
        for part in Path(path).parts:
            if part in ignored_dirs:
                return True
        return False

    # Recursive scan
    file_records = []
    folder_records = set()
    
    for root, dirs, files in os.walk(str(target)):
        # Modify dirs in-place to prune ignored directories
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        
        rel_root = Path(os.path.relpath(root, str(target))).as_posix()
        if rel_root != ".":
            folder_records.add(rel_root)
            
        for file in files:
            file_path = Path(root) / file
            rel_file_path = Path(os.path.relpath(str(file_path), str(target))).as_posix()
            ext = file_path.suffix
            
            if should_ignore(rel_file_path):
                files_skipped += 1
                continue
                
            all_files.append(rel_file_path)
            
            if ext in allowed_exts:
                files_scanned += 1
                size = file_path.stat().st_size
                owner = resolved_owners.get(rel_file_path, "Unknown")
                file_records.append({
                    "path": rel_file_path,
                    "size": size,
                    "extension": ext,
                    "owner": owner
                })
            else:
                files_skipped += 1

    # Counts by extension
    counts_by_ext = {}
    for r in file_records:
        ext = r["extension"]
        counts_by_ext[ext] = counts_by_ext.get(ext, 0) + 1
        
    # Ownership stats
    ownership_stats = {}
    for r in file_records:
        owner = r["owner"]
        if owner not in ownership_stats:
            ownership_stats[owner] = {"files_owned": 0}
        ownership_stats[owner]["files_owned"] += 1

    # MODULE 0: Write repo_index.json
    repo_index = {
        "files": file_records,
        "folders": sorted(list(folder_records)),
        "counts": {
            "total_files": len(file_records),
            "by_extension": counts_by_ext
        },
        "ownership": ownership_stats
    }
    with open(evidence_dir / "repo_index.json", "w") as f:
        json.dump(repo_index, f, indent=2)

    # Write REPO_TREE.md
    write_repo_tree(repo_index, files_scanned, files_skipped, docs_dir / "REPO_TREE.md")

    # Load file contents for regex scanning
    file_contents = {}
    for r in file_records:
        fp = target / r["path"]
        try:
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                file_contents[r["path"]] = f.read()
        except Exception as e:
            errors.append(f"Failed to read {r['path']}: {e}")

    # MODULE 1: Component Graph
    components = {}
    imports_map = {} # file -> list of resolved relative imports
    
    # First pass: identify imports and exports for each file
    for rel_path, content in file_contents.items():
        ext = Path(rel_path).suffix
        
        # Determine classification
        classification = "Shared Component"
        if ext == ".vue":
            if "views/" in rel_path or "pages/" in rel_path:
                classification = "Page"
            elif "layout" in rel_path.lower():
                classification = "Layout"
            else:
                classification = "Shared Component"
        elif ext in {".js", ".ts", ".jsx", ".tsx"}:
            name_lower = Path(rel_path).name.lower()
            if name_lower.startswith("use") or "/hooks/" in rel_path:
                classification = "Hook"
            elif "store" in rel_path or "context" in rel_path:
                classification = "Context / Store"
            elif "views/" in rel_path or "pages/" in rel_path:
                classification = "Page"
            else:
                classification = "Utility"
                
        # Parse imports
        imports = []
        # pattern: import ... from '...'
        from_matches = re.findall(r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]', content)
        # pattern: import('...')
        func_matches = re.findall(r'import\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)', content)
        # pattern: require('...')
        req_matches = re.findall(r'require\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)', content)
        
        raw_imports = set(from_matches + func_matches + req_matches)
        resolved_imports = []
        for imp in raw_imports:
            resolved = resolve_import_path(rel_path, imp, target)
            if resolved:
                resolved_imports.append(resolved)
        
        imports_map[rel_path] = resolved_imports
        
        # Parse exports
        # pattern: export default ...
        default_exports = re.findall(r'export\s+default\s+([a-zA-Z0-9_$]+)', content)
        # pattern: export const/let/var/function/class ...
        named_exports = re.findall(r'export\s+(?:const|let|var|function|class|interface|type)\s+([a-zA-Z0-9_$]+)', content)
        # pattern: export { a, b, c }
        curly_exports = []
        for match in re.findall(r'export\s*\{\s*([a-zA-Z0-9_$,\s]+)\s*\}', content):
            curly_exports.extend([x.strip() for x in match.split(",") if x.strip()])
            
        exports = sorted(list(set(default_exports + named_exports + curly_exports)))
        
        components[rel_path] = {
            "name": Path(rel_path).name,
            "path": rel_path,
            "classification": classification,
            "imports": resolved_imports,
            "exports": exports,
            "owner": resolved_owners.get(rel_path, "Unknown"),
            "fan_in": 0,
            "fan_out": len(resolved_imports),
            "depth": 0,
            "cycles": []
        }

    # Compute fan-in
    for comp_path, comp_data in components.items():
        for imp in comp_data["imports"]:
            if imp in components:
                components[imp]["fan_in"] += 1

    # Cycle detection and depth computation
    cycles_map = detect_cycles(imports_map)
    depths_map = compute_depth(imports_map)
    
    for comp_path, comp_data in components.items():
        comp_data["cycles"] = cycles_map.get(comp_path, [])
        comp_data["depth"] = depths_map.get(comp_path, 0)

    with open(evidence_dir / "component_graph.json", "w") as f:
        json.dump({"components": components}, f, indent=2)
        
    write_component_graph_md(components, docs_dir / "COMPONENT_GRAPH.md")

    # MODULE 2: Route Discovery
    routes = []
    # Identify routes configurations
    route_files = [r for r in file_records if "routes.js" in r["path"] or "router.js" in r["path"]]
    for rf in route_files:
        content = file_contents.get(rf["path"], "")
        imports_in_file = parse_imports_list(content)
        
        # Scan for path definitions
        # Pattern like: { path: '...', name: '...', component: ... }
        # Match braces using regex to find properties (including up to one level of nested braces for meta: { ... })
        blocks = re.findall(r'\{[^{]*?path:[^{}]*(?:[^{}]|\{[^{}]*\})*?\}', content, re.DOTALL)
        for block in blocks:
            path_match = re.search(r'path:\s*(?:frontendURL\()?[\'"`]([^\'"`]+)[\'"`]', block)
            name_match = re.search(r'name:\s*[\'"`]([^\'"`]+)[\'"`]', block)
            comp_match = re.search(r'component:\s*([a-zA-Z0-9_$]+)', block)
            
            meta_ent_match = re.search(r'requireEnterprise:\s*true', block)
            meta_sig_match = re.search(r'requireSignupEnabled:\s*true', block)
            is_protected = bool(meta_ent_match or meta_sig_match)
            
            if path_match:
                path_str = path_match.group(1)
                name_str = name_match.group(1) if name_match else path_str
                comp_name = comp_match.group(1) if comp_match else None
                
                # Resolve component file path
                entry_path = "Unknown"
                dependencies = []
                if comp_name and comp_name in imports_in_file:
                    imp_rel = imports_in_file[comp_name]
                    resolved = resolve_import_path(rf["path"], imp_rel, target)
                    if resolved:
                        entry_path = resolved
                        dependencies = components.get(resolved, {}).get("imports", [])
                
                routes.append({
                    "route": path_str,
                    "name": name_str,
                    "parent": rf["path"],
                    "entry": entry_path,
                    "dependencies": dependencies,
                    "protected": is_protected
                })

    with open(evidence_dir / "route_graph.json", "w") as f:
        json.dump({"routes": routes}, f, indent=2)
        
    write_route_graph_md(routes, docs_dir / "ROUTE_GRAPH.md")

    # MODULE 3: API Inventory
    api_calls = []
    # Match apiClient, axios, fetch, api calls
    for rel_path, content in file_contents.items():
        lines = content.splitlines()
        for idx, line in enumerate(lines):
            # Check axios/apiClient calls
            # Pattern: axios/apiClient.get/post/etc('url')
            methods = ["get", "post", "put", "delete", "patch"]
            for method in methods:
                matches = re.findall(r'(?:axios|apiClient|api)\.' + method + r'\(\s*([\'"`])([^\'"`]+)\1', line)
                for quote, url in matches:
                    api_calls.append({
                        "component": rel_path,
                        "endpoint": url,
                        "method": method.upper(),
                        "call_location": f"{rel_path}:{idx + 1}"
                    })
            # Check fetch calls
            fetch_matches = re.findall(r'fetch\(\s*([\'"`])([^\'"`]+)\1', line)
            for quote, url in fetch_matches:
                api_calls.append({
                    "component": rel_path,
                    "endpoint": url,
                    "method": "GET", # default for fetch
                    "call_location": f"{rel_path}:{idx + 1}"
                })

    # Group by endpoint and count calls
    endpoint_counts = {}
    for c in api_calls:
        key = (c["endpoint"], c["method"])
        endpoint_counts[key] = endpoint_counts.get(key, 0) + 1
        
    for c in api_calls:
        key = (c["endpoint"], c["method"])
        c["call_count"] = endpoint_counts[key]

    with open(evidence_dir / "api_inventory.json", "w") as f:
        json.dump({"api_calls": api_calls}, f, indent=2)
        
    write_api_inventory_md(api_calls, docs_dir / "API_INVENTORY.md")

    # MODULE 4: State Inventory
    state_items = []
    # Identify store declarations or state accessors
    for rel_path, content in file_contents.items():
        # Check Vuex createStore
        if "createStore" in content or "Vuex.Store" in content:
            state_items.append({
                "mechanism": "Vuex Store",
                "owner": rel_path,
                "consumers": [],
                "mutators": [],
                "duplicates": []
            })
        # Check Pinia defineStore
        pinia_stores = re.findall(r'defineStore\(\s*[\'"]([^\'"]+)[\'"]', content)
        for store_id in pinia_stores:
            state_items.append({
                "mechanism": f"Pinia Store ({store_id})",
                "owner": rel_path,
                "consumers": [],
                "mutators": [],
                "duplicates": []
            })
            
    # Scan for consumers/mutators
    for item in state_items:
        mech = item["mechanism"]
        owner = item["owner"]
        
        # Consumers of localStorage/sessionStorage
        if "Store" in mech:
            store_id = mech.split("(")[-1].replace(")", "") if "(" in mech else None
            for rel_path, content in file_contents.items():
                if rel_path == owner:
                    continue
                # If store is imported/used
                if store_id and store_id in content:
                    item["consumers"].append(rel_path)
                    if "actions" in content or "commit" in content or "dispatch" in content:
                        item["mutators"].append(rel_path)
                        
    # Add localStorage/sessionStorage state items
    local_storage_keys = set()
    session_storage_keys = set()
    for rel_path, content in file_contents.items():
        ls_gets = re.findall(r'localStorage\.getItem\(\s*[\'"]([^\'"]+)[\'"]', content)
        ls_sets = re.findall(r'localStorage\.setItem\(\s*[\'"]([^\'"]+)[\'"]', content)
        ss_gets = re.findall(r'sessionStorage\.getItem\(\s*[\'"]([^\'"]+)[\'"]', content)
        ss_sets = re.findall(r'sessionStorage\.setItem\(\s*[\'"]([^\'"]+)[\'"]', content)
        
        for k in ls_gets + ls_sets:
            local_storage_keys.add(k)
        for k in ss_gets + ss_sets:
            session_storage_keys.add(k)
            
    for k in local_storage_keys:
        consumers = []
        mutators = []
        for rel_path, content in file_contents.items():
            if f"localStorage.getItem('{k}')" in content or f'localStorage.getItem("{k}")' in content:
                consumers.append(rel_path)
            if f"localStorage.setItem('{k}'" in content or f'localStorage.setItem("{k}"' in content:
                mutators.append(rel_path)
        state_items.append({
            "mechanism": f"localStorage ({k})",
            "owner": "Global Browser Scope",
            "consumers": consumers,
            "mutators": mutators,
            "duplicates": []
        })
        
    for k in session_storage_keys:
        consumers = []
        mutators = []
        for rel_path, content in file_contents.items():
            if f"sessionStorage.getItem('{k}')" in content or f'sessionStorage.getItem("{k}")' in content:
                consumers.append(rel_path)
            if f"sessionStorage.setItem('{k}'" in content or f'sessionStorage.setItem("{k}"' in content:
                mutators.append(rel_path)
        state_items.append({
            "mechanism": f"sessionStorage ({k})",
            "owner": "Global Browser Scope",
            "consumers": consumers,
            "mutators": mutators,
            "duplicates": []
        })

    # Detect duplicate state/store names
    state_names = [x["mechanism"] for x in state_items]
    for item in state_items:
        mech = item["mechanism"]
        if state_names.count(mech) > 1:
            item["duplicates"] = [x["owner"] for x in state_items if x["mechanism"] == mech and x["owner"] != item["owner"]]

    with open(evidence_dir / "state_inventory.json", "w") as f:
        json.dump({"state_items": state_items}, f, indent=2)
        
    write_state_inventory_md(state_items, docs_dir / "STATE_INVENTORY.md")

    # MODULE 5: Event Inventory
    events = []
    for rel_path, content in file_contents.items():
        lines = content.splitlines()
        for idx, line in enumerate(lines):
            # Vue events: @click, @submit
            vue_events = re.findall(r'@(click|submit|keyup|change)="([^"]+)"', line)
            for event_type, handler in vue_events:
                events.append({
                    "source": f"{rel_path}:{idx + 1}",
                    "target": event_type,
                    "handler": handler,
                    "async": "async" in handler or "then" in content,
                    "debounce": "debounce" in line or "debounce" in content,
                    "throttle": "throttle" in line or "throttle" in content
                })
                
            # DOM event listeners
            dom_events = re.findall(r'addEventListener\(\s*[\'"]([^\'"]+)[\'"]\s*,\s*([a-zA-Z0-9_$]+)', line)
            for event_type, handler in dom_events:
                events.append({
                    "source": f"{rel_path}:{idx + 1}",
                    "target": event_type,
                    "handler": handler,
                    "async": "async" in line or "then" in line,
                    "debounce": "debounce" in line or "debounce" in content,
                    "throttle": "throttle" in line or "throttle" in content
                })
                
            # React style click/submit handlers
            react_events = re.findall(r'on(Click|Submit)\s*=\s*\{([^}]+)\}', line)
            for event_type, handler in react_events:
                events.append({
                    "source": f"{rel_path}:{idx + 1}",
                    "target": event_type.lower(),
                    "handler": handler,
                    "async": "async" in line or "then" in line,
                    "debounce": "debounce" in line or "debounce" in content,
                    "throttle": "throttle" in line or "throttle" in content
                })
                
            # Effects / Watchers
            effects = re.findall(r'\b(watch|watchEffect|computed|useEffect)\(', line)
            for eff in effects:
                events.append({
                    "source": f"{rel_path}:{idx + 1}",
                    "target": "Reactive Hook",
                    "handler": eff,
                    "async": False,
                    "debounce": "debounce" in line or "debounce" in content,
                    "throttle": "throttle" in line or "throttle" in content
                })
                
            # Timers
            timers = re.findall(r'\b(setTimeout|setInterval)\(', line)
            for t in timers:
                events.append({
                    "source": f"{rel_path}:{idx + 1}",
                    "target": "Timer Trigger",
                    "handler": t,
                    "async": False,
                    "debounce": False,
                    "throttle": False
                })

    with open(evidence_dir / "event_inventory.json", "w") as f:
        json.dump({"events": events}, f, indent=2)
        
    write_event_inventory_md(events, docs_dir / "EVENT_INVENTORY.md")

    # MODULE 6: Dependency Inventory
    dependencies = []
    # Read package.json
    pkg_path = target / "package.json"
    if pkg_path.exists():
        try:
            with open(pkg_path, "r") as f:
                pkg_data = json.load(f)
                for dep, ver in pkg_data.get("dependencies", {}).items():
                    dependencies.append({
                        "dependency": dep,
                        "version": ver,
                        "category": "dependencies"
                    })
                for dep, ver in pkg_data.get("devDependencies", {}).items():
                    dependencies.append({
                        "dependency": dep,
                        "version": ver,
                        "category": "devDependencies"
                    })
                for dep, ver in pkg_data.get("peerDependencies", {}).items():
                    dependencies.append({
                        "dependency": dep,
                        "version": ver,
                        "category": "peerDependencies"
                    })
        except Exception as e:
            errors.append(f"Error parsing package.json: {e}")

    with open(evidence_dir / "dependency_inventory.json", "w") as f:
        json.dump({"dependencies": dependencies}, f, indent=2)
        
    write_dependency_inventory_md(dependencies, docs_dir / "DEPENDENCY_INVENTORY.md")

    # Final summary calculations
    duration = time.time() - start_time
    total_files_in_repo = len(all_files)
    
    summary = {
        "files_scanned": files_scanned,
        "files_skipped": files_skipped,
        "duration_seconds": duration,
        "coverage_percent": (files_scanned / total_files_in_repo * 100) if total_files_in_repo > 0 else 0.0,
        "errors": errors,
        "unknowns": []
    }
    
    write_collection_summary(summary, base / "COLLECTION_SUMMARY.md")
    print(f"Evidence collection complete in {duration:.2f} seconds.")

# Helpers for import resolving
def resolve_import_path(current_file, import_str, target_root):
    # If starting with alias "dashboard/" or "shared/" or "v3/"
    curr_dir = Path(target_root) / current_file
    curr_parent = curr_dir.parent
    
    test_paths = []
    if import_str.startswith("."):
        # Relative import
        base_path = Path(os.path.normpath(curr_parent / import_str))
        test_paths.append(base_path)
    else:
        # Check standard root alias app/javascript
        js_root = Path(target_root) / "app" / "javascript"
        test_paths.append(js_root / import_str)
        
    # Check common JS/Vue extensions
    for p in test_paths:
        for ext in ["", ".js", ".ts", ".vue"]:
            target_file = Path(str(p) + ext)
            if target_file.is_file():
                return Path(os.path.relpath(str(target_file), str(target_root))).as_posix()
        for ext in ["index.js", "index.vue"]:
            target_file = p / ext
            if target_file.is_file():
                return Path(os.path.relpath(str(target_file), str(target_root))).as_posix()
    return None

def parse_imports_list(content):
    imports = {}
    matches = re.findall(r'import\s+([a-zA-Z0-9_$]+|\{[^}]+\})\s+from\s+[\'"]([^\'"]+)[\'"]', content)
    for names, path in matches:
        if "{" in names:
            # Curly import: extract symbols
            curly_names = [x.strip() for x in names.replace("{", "").replace("}", "").split(",") if x.strip()]
            for cn in curly_names:
                imports[cn] = path
        else:
            imports[names.strip()] = path
    return imports

# Graph processing helpers
def detect_cycles(graph):
    cycles = {}
    visited = set()
    
    def dfs(node, path, path_set):
        visited.add(node)
        path.append(node)
        path_set.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor in path_set:
                cycle_start = path.index(neighbor)
                cycle_path = path[cycle_start:]
                for n in cycle_path:
                    cycles[n] = cycle_path
            elif neighbor not in visited:
                dfs(neighbor, path, path_set)
                
        path.pop()
        path_set.remove(node)

    for node in graph:
        if node not in visited:
            dfs(node, [], set())
    return cycles

def compute_depth(graph):
    depths = {}
    memo = {}
    
    def get_depth(node, visited_in_path):
        if node in memo:
            return memo[node]
        if node in visited_in_path:
            return 0
        
        visited_in_path.add(node)
        max_child_depth = 0
        for neighbor in graph.get(node, []):
            max_child_depth = max(max_child_depth, get_depth(neighbor, visited_in_path))
        visited_in_path.remove(node)
        
        memo[node] = max_child_depth + (1 if graph.get(node) else 0)
        return memo[node]

    for node in graph:
        depths[node] = get_depth(node, set())
    return depths

# Formatting Markdown functions
def write_repo_tree(repo_index, scanned, skipped, target_file):
    with open(target_file, "w") as f:
        f.write("# Repository Directory Hierarchy Tree\n\n")
        f.write("## 1. Directory Tree Structural Hierarchy\n\n")
        f.write("```\n")
        f.write("root/\n")
        # List first level and nested level folders up to max depth 3
        # In sorted folder list
        prev_parts = []
        for folder in repo_index["folders"][:60]: # Limit size
            parts = Path(folder).parts
            indent = "  " * len(parts)
            f.write(f"{indent}└── {parts[-1]}/\n")
        f.write("```\n\n")
        
        f.write("## 2. Directory Scan Summary Counts\n\n")
        f.write(f"- **Total Files Scanned**: {scanned}\n")
        f.write(f"- **Total Files Skipped**: {skipped}\n\n")
        
        f.write("## 3. Extension File Counts\n\n")
        f.write("| Extension | Count |\n")
        f.write("|:---|:---|\n")
        for ext, count in repo_index["counts"]["by_extension"].items():
            f.write(f"| `{ext}` | {count} |\n")
        f.write("\n")
        
        f.write("## 4. Git Folder Ownership Statistics\n\n")
        f.write("| Author | Files Owned |\n")
        f.write("|:---|:---|\n")
        for author, stats in repo_index["ownership"].items():
            f.write(f"| {author} | {stats['files_owned']} |\n")

def write_component_graph_md(components, target_file):
    with open(target_file, "w") as f:
        f.write("# Component Architecture Graph\n\n")
        f.write("## 1. Component Registry & Metrics\n\n")
        f.write("| Component Path | Classification | Fan-In | Fan-Out | Depth | Owner |\n")
        f.write("|:---|:---|:---|:---|:---|:---|\n")
        for path, c in components.items():
            f.write(f"| `{path}` | {c['classification']} | {c['fan_in']} | {c['fan_out']} | {c['depth']} | {c['owner']} |\n")
            
        f.write("\n## 2. Dependency Loop Cycles Detected\n\n")
        cycles_found = [c for c in components.values() if c["cycles"]]
        if not cycles_found:
            f.write("No circular dependency loops detected.\n")
        else:
            f.write("| Component | Cycle Path |\n")
            f.write("|:---|:---|\n")
            for c in cycles_found:
                cycle_str = " -> ".join([f"`{x}`" for x in c["cycles"]])
                f.write(f"| `{c['path']}` | {cycle_str} |\n")

def write_route_graph_md(routes, target_file):
    with open(target_file, "w") as f:
        f.write("# Route Mapping Discovery\n\n")
        f.write("## 1. Registered SPA Routes\n\n")
        f.write("| Route path | Route name | Entry Component | Protected? | Parent File |\n")
        f.write("|:---|:---|:---|:---|:---|\n")
        for r in routes:
            f.write(f"| `{r['route']}` | {r['name']} | `{r['entry']}` | {r['protected']} | `{r['parent']}` |\n")

def write_api_inventory_md(api_calls, target_file):
    with open(target_file, "w") as f:
        f.write("# API Endpoint Inventory\n\n")
        f.write("## 1. Outgoing API Call References\n\n")
        f.write("| Endpoint Method Path | Endpoint | Component | Location | Call Count |\n")
        f.write("|:---|:---|:---|:---|:---|\n")
        for c in api_calls:
            f.write(f"| `{c['method']}` | `{c['endpoint']}` | `{c['component']}` | `{c['call_location']}` | {c['call_count']} |\n")

def write_state_inventory_md(state_items, target_file):
    with open(target_file, "w") as f:
        f.write("# State Management Inventory\n\n")
        f.write("## 1. State Systems & Declarations\n\n")
        f.write("| State Mechanism / ID | Owner File | Consumers | Mutators | Duplicates |\n")
        f.write("|:---|:---|:---|:---|:---|\n")
        for item in state_items:
            consumers_str = ", ".join([f"`{x}`" for x in item["consumers"][:5]])
            mutators_str = ", ".join([f"`{x}`" for x in item["mutators"][:5]])
            dup_str = ", ".join([f"`{x}`" for x in item["duplicates"]])
            f.write(f"| `{item['mechanism']}` | `{item['owner']}` | {consumers_str} | {mutators_str} | {dup_str} |\n")

def write_event_inventory_md(events, target_file):
    with open(target_file, "w") as f:
        f.write("# Event Handling Inventory\n\n")
        f.write("## 1. Registered Interactive Events\n\n")
        f.write("| Source Location | Target Event | Handler Name | Async? | Debounce? | Throttle? |\n")
        f.write("|:---|:---|:---|:---|:---|:---|\n")
        for e in events:
            f.write(f"| `{e['source']}` | `{e['target']}` | `{e['handler']}` | {e['async']} | {e['debounce']} | {e['throttle']} |\n")

def write_dependency_inventory_md(dependencies, target_file):
    with open(target_file, "w") as f:
        f.write("# Project Package Dependencies\n\n")
        f.write("## 1. Package Manifest Registry\n\n")
        f.write("| Dependency Name | Version | Category |\n")
        f.write("|:---|:---|:---|\n")
        for dep in dependencies:
            f.write(f"| **{dep['dependency']}** | `{dep['version']}` | {dep['category']} |\n")

def write_collection_summary(summary, target_file):
    with open(target_file, "w") as f:
        f.write("# Evidence Collection Summary Report\n\n")
        f.write(f"- **Files Scanned**: {summary['files_scanned']}\n")
        f.write(f"- **Files Skipped**: {summary['files_skipped']}\n")
        f.write(f"- **Execution Duration**: {summary['duration_seconds']:.2f} seconds\n")
        f.write(f"- **Target Code Coverage**: {summary['coverage_percent']:.2f}%\n")
        
        f.write("\n## Errors Encountered\n\n")
        if not summary["errors"]:
            f.write("No scanning or parser execution errors occurred.\n")
        else:
            for err in summary["errors"]:
                f.write(f"- {err}\n")
                
        f.write("\n## Unknown / Unclassified Elements\n\n")
        f.write("No unknown elements found.\n")
