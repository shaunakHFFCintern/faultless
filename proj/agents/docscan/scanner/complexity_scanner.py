import re
import json
from pathlib import Path

def scan_complexity(target_path, base_dir, file_records, file_contents, api_calls):
    target = Path(target_path).resolve()
    base = Path(base_dir).resolve()
    
    # Pre-map API calls by component path for fast lookup
    api_by_component = {}
    for c in api_calls:
        comp = c.get("component")
        if comp not in api_by_component:
            api_by_component[comp] = []
        api_by_component[comp].append(c)

    # 1. Load complexity thresholds config
    rules_path = base / "config" / "complexity_rules.json"
    high_thresholds = {
        "lines_of_code": 300,
        "render_tree_depth": 4,
        "conditional_rendering_count": 10,
        "import_count": 15,
        "lifecycle_effect_count": 4,
        "reactive_logic_count": 8,
        "event_listener_count": 8
    }
    medium_thresholds = {
        "lines_of_code": 150,
        "render_tree_depth": 3,
        "import_count": 8,
        "reactive_logic_count": 4
    }

    if rules_path.exists():
        try:
            with open(rules_path, "r", encoding="utf-8") as f:
                rules_data = json.load(f)
                high_thresholds = rules_data.get("high_thresholds", high_thresholds)
                medium_thresholds = rules_data.get("medium_thresholds", medium_thresholds)
        except Exception as e:
            print(f"Error loading complexity_rules.json: {e}")

    results = []

    # Sort files alphabetically to ensure stable ID assignment
    sorted_files = sorted(file_records, key=lambda x: x["path"])

    for idx, record in enumerate(sorted_files):
        rel_path = record["path"]
        content = file_contents.get(rel_path, "")
        
        # Calculate raw metrics
        lines = content.splitlines()
        loc = len(lines)
        
        # Imports & Exports
        imports_count = len(re.findall(r'\bimport\b|\brequire\s*\(', content))
        exports_count = len(re.findall(r'\bexport\b|\bmodule\.exports\b', content))
        
        # Function declarations
        function_count = len(re.findall(r'\bfunction\b|\bclass\s+\w+|\bconst\s+\w+\s*=\s*\([^)]*\)\s*=>|\b\w+\s*\([^)]*\)\s*\{', content))
        
        # Reactive Logic
        reactive_logic_count = len(re.findall(r'\buse[A-Z]\w*\b|\bref\b|\breactive\b|\bsignal\b', content))
        
        # Lifecycle effect count
        lifecycle_effect_count = len(re.findall(r'\buseEffect\b|\bwatch\b|\bwatchEffect\b|\bcomputed\b|\bngOnInit\b|\bngAfterViewInit\b', content))
        
        # API calls in this file
        file_apis = api_by_component.get(rel_path, [])
        api_call_count = len(file_apis)
        
        # State usage count
        state_usage_count = len(re.findall(r'\buseState\b|\bstate\b|\bstore\b|\bcontext\b|\bcreateStore\b|\bdefineStore\b', content))
        
        # Event listener count
        event_listener_count = len(re.findall(r'@click|@submit|onClick|onSubmit|addEventListener\b', content))
        
        # Child Component count
        child_component_count = len(re.findall(r'<\s*[A-Z]\w+', content))
        
        # Render Tree Nesting Depth
        render_tree_depth = calculate_nesting_depth(content)
        
        # Conditional Rendering count
        conditional_rendering_count = len(re.findall(r'\bv-if\b|\bv-show\b|\*ngIf\b|\?.*?:|\&\&', content))
        
        # Custom hook count
        all_hooks = re.findall(r'\buse[A-Z]\w*\b', content)
        standard_hooks = {"useState", "useEffect", "useContext", "useReducer", "useCallback", "useMemo", "useRef", "useImperativeHandle", "useLayoutEffect", "useDebugValue"}
        custom_hook_count = len([h for h in all_hooks if h not in standard_hooks])
        
        # Context usage count
        context_usage_count = len(re.findall(r'\buseContext\b|provide\s*\(|inject\s*\(|\bInject\b', content))
        
        # Memoization usage count
        memoization_usage_count = len(re.findall(r'\buseMemo\b|\buseCallback\b|\bmemo\b|\bcomputed\b', content))
        
        # Estimate Prop declaration count
        props_matches = len(re.findall(r'\bprops\b|defineProps|@Input', content))
        
        # Check if multiple API client frameworks are used in this file
        client_types = set()
        for c in file_apis:
            client_types.add(c.get("metadata", {}).get("evidence_type", "Unknown"))
        multiple_api_clients = len(client_types) > 1

        metrics = {
            "lines_of_code": loc,
            "import_count": imports_count,
            "export_count": exports_count,
            "function_count": function_count,
            "reactive_logic_count": reactive_logic_count,
            "lifecycle_effect_count": lifecycle_effect_count,
            "api_call_count": api_call_count,
            "state_usage_count": state_usage_count,
            "event_listener_count": event_listener_count,
            "child_component_count": child_component_count,
            "render_tree_depth": render_tree_depth,
            "conditional_rendering_count": conditional_rendering_count,
            "custom_hook_count": custom_hook_count,
            "context_usage_count": context_usage_count,
            "memoization_usage_count": memoization_usage_count
        }

        # Classify Complexity using dynamically loaded thresholds
        threshold_violations = []
        for key, val in high_thresholds.items():
            if metrics.get(key, 0) > val:
                threshold_violations.append(f"{key} > {val} ({metrics[key]})")
                
        if threshold_violations:
            classification = "HIGH"
        else:
            medium_violations = []
            for key, val in medium_thresholds.items():
                if metrics.get(key, 0) > val:
                    medium_violations.append(f"{key} > {val} ({metrics[key]})")
            if medium_violations:
                classification = "MEDIUM"
                threshold_violations = medium_violations
            else:
                classification = "LOW"

        # Construct risk signals facts
        risk_signals = {
            "LARGE_COMPONENT": loc > high_thresholds.get("lines_of_code", 300),
            "HIGH_EFFECT_COUNT": lifecycle_effect_count > high_thresholds.get("lifecycle_effect_count", 4),
            "HIGH_IMPORT_COUNT": imports_count > high_thresholds.get("import_count", 15),
            "HIGH_PROP_COUNT": props_matches > 10,
            "MULTIPLE_API_CLIENTS": multiple_api_clients
        }

        results.append({
            "id": f"COMP_{idx+1:04d}",
            "path": rel_path,
            "source_location": {
                "file": rel_path,
                "line": 1
            },
            "metrics": metrics,
            "threshold_violations": threshold_violations,
            "classification": classification,
            "risk_signals": risk_signals
        })

    # Write complexity_inventory.json
    evidence_dir = base / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(evidence_dir / "complexity_inventory.json", "w", encoding="utf-8") as f:
            json.dump({"files": results}, f, indent=2)
    except Exception as e:
        print(f"Error writing complexity_inventory.json: {e}")

def calculate_nesting_depth(content):
    cleaned = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)
    cleaned = re.sub(r'//.*', '', cleaned)
    
    max_depth = 0
    current_depth = 0
    
    tag_pattern = r'<(/?[a-zA-Z0-9_:\-]+)(?:\s+[^>]*?)?(/?)>'
    
    for m in re.finditer(tag_pattern, cleaned):
        tag_name = m.group(1)
        is_self_closing = m.group(2) == "/"
        
        if tag_name.lower() in {"img", "br", "hr", "input", "meta", "link", "col", "embed", "param", "source", "track", "wbr"}:
            is_self_closing = True
            
        if tag_name.startswith("/"):
            current_depth = max(0, current_depth - 1)
        elif not is_self_closing:
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
                
    return max_depth
