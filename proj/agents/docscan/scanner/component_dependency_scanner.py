import re
import json
from pathlib import Path

def scan_component_dependencies(target_path, base_dir, file_records, file_contents):
    target = Path(target_path).resolve()
    base = Path(base_dir).resolve()
    
    # Map file paths for quick lookup
    all_files = {r["path"]: r for r in file_records}
    
    dependencies = []
    
    # Sort files to guarantee deterministic order
    sorted_files = sorted(file_records, key=lambda x: x["path"])
    
    for record in sorted_files:
        parent_path = record["path"]
        content = file_contents.get(parent_path, "")
        lines = content.splitlines()
        
        # Statically extract imports
        # e.g. import MyComponent from './MyComponent.vue'
        imports = re.findall(r'\bimport\s+(\w+)\s+from\s+[\'"]([^\'"]+)[\'"]', content)
        
        # Also match braces imports: import { MyComponent } from './MyComponent'
        braces_imports = re.findall(r'\bimport\s*\{\s*(\w+)\s*\}\s*from\s+[\'"]([^\'"]+)[\'"]', content)
        all_imports = imports + braces_imports
        
        children = []
        
        for comp_name, import_path in all_imports:
            # Resolve imported file relative to the parent file's directory
            parent_dir = Path(parent_path).parent
            
            # Simple path resolution: try suffix extensions if missing
            resolved_rel = None
            for ext in ["", ".vue", ".js", ".jsx", ".ts", ".tsx"]:
                candidate = Path(target / parent_dir / (import_path + ext)).resolve()
                try:
                    # Get path relative to the target codebase root
                    rel_candidate = str(candidate.relative_to(target))
                    if rel_candidate in all_files:
                        resolved_rel = rel_candidate
                        break
                except ValueError:
                    pass
            
            if resolved_rel:
                # Confirm the child component is used as a tag in the template/JSX
                # e.g. <MyComponent or <my-component or <myComponent
                kebab_name = re.sub(r'(?<!^)(?=[A-Z])', '-', comp_name).lower()
                tag_patterns = [
                    r'<\s*' + re.escape(comp_name) + r'\b',
                    r'<\s*' + re.escape(kebab_name) + r'\b'
                ]
                
                is_used = False
                use_line = 1
                for l_idx, l_content in enumerate(lines):
                    # Skip import statement lines when scanning for tag usage
                    if "import" in l_content and comp_name in l_content:
                        continue
                    if any(re.search(pat, l_content) for pat in tag_patterns):
                        is_used = True
                        use_line = l_idx + 1
                        break
                
                # If tag is not found, fallback to import statement line number
                if not is_used:
                    for l_idx, l_content in enumerate(lines):
                        if "import" in l_content and comp_name in l_content:
                            is_used = True
                            use_line = l_idx + 1
                            break
                            
                if is_used:
                    children.append({
                        "child": resolved_rel,
                        "location": f"{parent_path}:{use_line}"
                    })
                    
        if children:
            # Sort children by path for stability
            children = sorted(children, key=lambda x: x["child"])
            dependencies.append({
                "parent": parent_path,
                "children": children
            })
            
    # Write component_dependency_inventory.json
    evidence_dir = base / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    try:
        with open(evidence_dir / "component_dependency_inventory.json", "w", encoding="utf-8") as f:
            json.dump({"dependencies": dependencies}, f, indent=2)
    except Exception as e:
        print(f"Error writing component_dependency_inventory.json: {e}")
