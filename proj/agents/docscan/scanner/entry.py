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
    target = load_target()

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
    except Exception as e:
        print(f"Error executing evidence collector: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
