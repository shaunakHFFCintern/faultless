from pathlib import Path
from framework_detector import detect_framework
from repo_loader import load_repository
from doc_generator import (
    write_discovery,
    write_exec_summary
)

BASE_DIR = Path(__file__).resolve().parent.parent

def load_target():
    config = BASE_DIR / "config" / "target_repo.txt"

    with open(config, "r") as f:
        return f.read().strip()


def main():
    target_raw = load_target()
    target_path = Path(target_raw).expanduser()
    if not target_path.is_absolute():
        target_path = (BASE_DIR.parent.parent.parent / target_path).resolve()
    else:
        target_path = target_path.resolve()
    target = str(target_path)

    print("\nLoaded Target:")
    print(repr(target))

    print("\n=== DOCSCAN ===")

    print("\nTarget:")
    print(target)

    result = load_repository(target)

    framework = detect_framework(target)
    output = write_discovery(
        target,
        framework,
        result
    )
    summary = write_exec_summary(
        target,
        framework,
        result
    )

    print("\nFramework:")
    print(framework)

    print("\nFolders:")

    for folder in result["folders"]:
        print(f"  • {folder}")

    print("\nFiles:")

    for file in result["files"]:
        print(f"  • {file}")

    print("\nGenerated:")
    print(output)
    print(summary)

    print("\n=== STARTING EVIDENCE COLLECTION ===")
    try:
        from evidence_collector import collect_evidence
        collect_evidence(target, BASE_DIR)
        
        # Load generated files to pass to complexity/interaction scanners
        import json
        evidence_dir = BASE_DIR / "evidence"
        
        # Load file_records from repo_index.json
        with open(evidence_dir / "repo_index.json", "r", encoding="utf-8") as f:
            repo_index = json.load(f)
            file_records = repo_index.get("files", [])
            
        # Load api_calls from api_inventory.json
        with open(evidence_dir / "api_inventory.json", "r", encoding="utf-8") as f:
            api_inventory = json.load(f)
            api_calls = api_inventory.get("api_calls", [])
            
        # Load raw file contents for static regex scans
        file_contents = {}
        for r in file_records:
            fp = Path(target) / r["path"]
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    file_contents[r["path"]] = f.read()
            except Exception as e:
                print(f"Failed to read file for scanner integration {r['path']}: {e}")

        # Run Complexity Scanner
        print("Running Complexity Scanner...")
        from complexity_scanner import scan_complexity
        scan_complexity(target, BASE_DIR, file_records, file_contents, api_calls)
        
        # Run Interaction Flow Scanner
        print("Running Interaction Flow Scanner...")
        from interaction_flow_scanner import scan_interaction_flows
        scan_interaction_flows(target, BASE_DIR, file_records, file_contents, api_calls)
        
        # Run State Relationship Scanner
        print("Running State Relationship Scanner...")
        from state_relationship_scanner import scan_state_relationships
        scan_state_relationships(target, BASE_DIR, file_records, file_contents)
        
        # Run Component Dependency Scanner
        print("Running Component Dependency Scanner...")
        from component_dependency_scanner import scan_component_dependencies
        scan_component_dependencies(target, BASE_DIR, file_records, file_contents)
        
        print("All extended evidence collection completed successfully.")
    except Exception as e:
        print(f"Error executing evidence collector: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
