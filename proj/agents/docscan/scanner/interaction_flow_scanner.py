import re
import json
from pathlib import Path

def scan_interaction_flows(target_path, base_dir, file_records, file_contents, api_calls):
    target = Path(target_path).resolve()
    base = Path(base_dir).resolve()
    
    # Pre-map API endpoints called by each component
    api_by_component = {}
    for c in api_calls:
        comp = c.get("component")
        if comp not in api_by_component:
            api_by_component[comp] = []
        api_by_component[comp].append(c)

    interactions = []

    # Sort files to ensure deterministic Flow IDs
    sorted_files = sorted(file_records, key=lambda x: x["path"])
    flow_idx = 1

    for record in sorted_files:
        rel_path = record["path"]
        content = file_contents.get(rel_path, "")
        lines = content.splitlines()
        
        # 1. Statically extract event bindings
        vue_events = re.findall(r'@(click|submit|keyup|change)="([^"]+)"', content)
        react_events = re.findall(r'\bon(Click|Submit)\s*=\s*\{([^}]+)\}', content)
        dom_events = re.findall(r'addEventListener\(\s*[\'"]([^\'"]+)[\'"]\s*,\s*([a-zA-Z0-9_$]+)', content)
        
        bindings = []
        for event, handler in vue_events:
            bindings.append((event, handler.strip().replace("()", "")))
        for event, handler in react_events:
            bindings.append((event.lower(), handler.strip().replace("()", "")))
        for event, handler in dom_events:
            bindings.append((event, handler.strip()))
            
        bindings = list(set(bindings))
        
        for event, handler in sorted(bindings, key=lambda x: (x[0], x[1])):
            handler_escaped = re.escape(handler)
            handler_def_pattern = r'\b' + handler_escaped + r'\b\s*(?:\(|:|=)'
            
            # Statically find starting line of the handler
            handler_line = 1
            for l_idx, l_content in enumerate(lines):
                if re.search(handler_def_pattern, l_content):
                    handler_line = l_idx + 1
                    break

            handler_lines = []
            m = re.search(handler_def_pattern, content)
            if m:
                start_pos = m.start()
                block = content[start_pos:start_pos + 1000]
                handler_lines = block.splitlines()
            else:
                handler_lines = lines
                
            block_text = "\n".join(handler_lines)
            
            # Trace State Mutations in the handler block
            state_mutations = []
            if re.search(r'\bcommit\b|\bdispatch\b', block_text):
                state_mutations.append("Store Mutation (Vuex)")
            pinia_matches = re.findall(r'\b(\w+)\s*\.\s*(?:\$patch|value\s*=|\w+\s*=)', block_text)
            for pm in pinia_matches:
                if pm not in {"this", "window", "console", "document"}:
                    state_mutations.append(f"State Variable Write ({pm})")
            react_setters = re.findall(r'\b(set[A-Z]\w*)\b\s*\(', block_text)
            for rs in react_setters:
                state_mutations.append(f"React State Setter ({rs})")
                
            state_mutations = sorted(list(set(state_mutations)))
            
            # Trace API Calls in the handler block
            apis_called = []
            file_apis = api_by_component.get(rel_path, [])
            for api in file_apis:
                endpoint = api.get("endpoint")
                if endpoint in block_text or api.get("method") in block_text:
                    apis_called.append(f"{api.get('method')}:{endpoint}")
            apis_called = sorted(list(set(apis_called)))
            
            # Trace Navigations in the handler block
            navigations = []
            if re.search(r'\brouter\.push\b|\bthis\.\$router\.push\b|\bnavigate\b', block_text):
                navigations.append("SPA Router Navigation")
            if re.search(r'\bwindow\.location\.href\b|\blocation\b\s*=', block_text):
                navigations.append("Window Location Redirect")
            navigations = sorted(list(set(navigations)))
            
            # Trace Affected Component References
            affected_component_refs = []
            imports = re.findall(r'\bimport\s+(?:[a-zA-Z0-9_$]+|\{[^}]+\})\s+from\s+[\'"]([^\'"]+)[\'"]', content)
            for imp in imports:
                if imp.startswith(".") or "components" in imp:
                    affected_component_refs.append(Path(imp).name)
            affected_component_refs = sorted(list(set(affected_component_refs)))

            interactions.append({
                "id": f"FLOW_{flow_idx:04d}",
                "component": rel_path,
                "source_location": {
                    "file": rel_path,
                    "line": handler_line
                },
                "chain": {
                    "event": event,
                    "handler": handler,
                    "state_mutations": state_mutations,
                    "api_calls": apis_called,
                    "navigation": navigations,
                    "affected_component_refs": affected_component_refs
                }
            })
            flow_idx += 1
            
    # Write interaction_inventory.json
    evidence_dir = base / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    try:
        with open(evidence_dir / "interaction_inventory.json", "w", encoding="utf-8") as f:
            json.dump({"interactions": interactions}, f, indent=2)
    except Exception as e:
        print(f"Error writing interaction_inventory.json: {e}")
