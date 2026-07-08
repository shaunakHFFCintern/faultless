import re
import json
from pathlib import Path

def scan_state_relationships(target_path, base_dir, file_records, file_contents):
    target = Path(target_path).resolve()
    base = Path(base_dir).resolve()
    
    stores = []
    
    # Find Pinia Stores
    for rel_path, content in file_contents.items():
        pinia_stores = re.findall(r'defineStore\(\s*[\'"]([^\'"]+)[\'"]', content)
        for store_id in pinia_stores:
            stores.append({
                "name": store_id,
                "type": "Pinia Store",
                "file": rel_path,
                "pattern": store_id
            })
            
        # Find Vuex Stores
        if "createStore" in content or "Vuex.Store" in content:
            stores.append({
                "name": "Vuex Store",
                "type": "Vuex Store",
                "file": rel_path,
                "pattern": r'\$store|commit|dispatch'
            })
            
        # Find React Contexts
        react_contexts = re.findall(r'createContext\b', content)
        if react_contexts:
            context_names = re.findall(r'const\s+(\w+Context)\s*=\s*createContext(?:<[^>]*>)?', content)
            for cname in context_names:
                stores.append({
                    "name": cname,
                    "type": "React Context",
                    "file": rel_path,
                    "pattern": cname
                })

    stores = sorted(stores, key=lambda x: (x["name"], x["file"]))
    
    relationships = []
    
    for idx, store in enumerate(stores):
        consumers = []
        pattern = store["pattern"]
        
        # Statically locate store declaration line in the declaring file
        decl_line = 1
        decl_lines = file_contents[store["file"]].splitlines()
        for l_idx, l_content in enumerate(decl_lines):
            if any(k in l_content for k in ["defineStore", "createStore", "createContext", "Vuex.Store"]):
                decl_line = l_idx + 1
                break

        for rel_path, content in file_contents.items():
            if rel_path == store["file"]:
                continue
                
            is_consumer = False
            hook_name = f"use{store['name'][0].upper()}{store['name'][1:]}Store"
            if store["type"] == "Pinia Store":
                if pattern in content or hook_name in content:
                    is_consumer = True
            elif store["type"] == "React Context":
                context_hook = "use" + store["name"].replace("Context", "")
                if pattern in content or context_hook in content:
                    is_consumer = True
            elif store["type"] == "Vuex Store":
                if re.search(pattern, content):
                    is_consumer = True
                    
            if is_consumer:
                # Statically locate store consumption line in the consuming file
                cons_line = 1
                cons_lines = content.splitlines()
                for l_idx, l_content in enumerate(cons_lines):
                    if store["type"] == "Pinia Store":
                        if hook_name in l_content or store["name"] in l_content:
                            cons_line = l_idx + 1
                            break
                    elif store["type"] == "Vuex Store":
                        if re.search(r'\$store|commit|dispatch', l_content):
                            cons_line = l_idx + 1
                            break
                    elif store["type"] == "React Context":
                        context_hook = "use" + store["name"].replace("Context", "")
                        if store["name"] in l_content or "useContext" in l_content or context_hook in l_content:
                            cons_line = l_idx + 1
                            break

                access_type = "read-only"
                if store["type"] == "Pinia Store":
                    inst_var = "store"
                    m_var = re.search(r'const\s+(\w+)\s*=\s*' + re.escape(hook_name) + r'\b', content)
                    if m_var:
                        inst_var = m_var.group(1)
                    
                    if "$patch" in content or re.search(r'\b' + re.escape(inst_var) + r'\b\.\w+\s*=', content):
                        access_type = "read-write"
                    elif re.search(r'\b' + re.escape(inst_var) + r'\b\.\w+\(', content):
                        access_type = "read-write"
                elif store["type"] == "Vuex Store":
                    if "commit" in content or "dispatch" in content:
                        access_type = "read-write"
                elif store["type"] == "React Context":
                    context_hook = "use" + store["name"].replace("Context", "")
                    if re.search(r'\b(?:set|add|update|delete|mut)\w*', content, re.IGNORECASE) and context_hook in content:
                        access_type = "read-write"
                        
                consumers.append({
                    "file": rel_path,
                    "access_type": access_type,
                    "source_location": {
                        "file": rel_path,
                        "line": cons_line
                    }
                })
                
        consumers = sorted(consumers, key=lambda x: x["file"])
        
        relationships.append({
            "id": f"STORE_{idx+1:04d}",
            "store_or_context": store["name"],
            "type": store["type"],
            "file": store["file"],
            "source_location": {
                "file": store["file"],
                "line": decl_line
            },
            "consumers": consumers
        })

    # Write state_relationship_inventory.json
    evidence_dir = base / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    try:
        with open(evidence_dir / "state_relationship_inventory.json", "w", encoding="utf-8") as f:
            json.dump({"relationships": relationships}, f, indent=2)
    except Exception as e:
        print(f"Error writing state_relationship_inventory.json: {e}")
