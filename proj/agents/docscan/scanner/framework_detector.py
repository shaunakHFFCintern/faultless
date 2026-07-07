import json
import sys
from pathlib import Path

# Add the parent directory of detectors to path if not present
sys.path.append(str(Path(__file__).resolve().parent))

import detectors.react as react_detector
import detectors.vue as vue_detector
import detectors.angular as angular_detector
import detectors.nextjs as nextjs_detector

def detect_framework(repo_path):
    repo = Path(repo_path).expanduser().resolve()
    
    # 1. Backwards compatible framework detection
    files = [x.name for x in repo.iterdir() if x.is_file()]
    
    primary_framework = "unknown"
    if "hooks.py" in files:
        primary_framework = "frappe"
    elif "package.json" in files:
        primary_framework = "node"
    elif "manage.py" in files:
        primary_framework = "django"
    elif "pyproject.toml" in files:
        primary_framework = "python"

    # 2. Parse package.json for plugin detectors
    package_data = {}
    package_json_path = repo / "package.json"
    if package_json_path.exists():
        try:
            with open(package_json_path, "r", encoding="utf-8") as f:
                package_data = json.load(f)
        except Exception as e:
            print(f"Error parsing package.json in detector: {e}")

    # Prepare file records from repository (shallow scan for detector fallback)
    file_records = []
    for item in repo.rglob("*"):
        if item.is_file():
            # Skip common noise dirs
            if not any(part in item.parts for part in {".git", "node_modules", "dist", "build"}):
                file_records.append({
                    "path": str(item.relative_to(repo)),
                    "extension": item.suffix
                })

    # Run detectors
    technologies = []
    technologies.extend(react_detector.detect(package_data, file_records))
    technologies.extend(vue_detector.detect(package_data, file_records))
    technologies.extend(angular_detector.detect(package_data, file_records))
    technologies.extend(nextjs_detector.detect(package_data, file_records))

    # Write framework_inventory.json
    evidence_dir = Path(__file__).resolve().parent.parent / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    
    inventory = {
        "technologies": technologies
    }

    try:
        with open(evidence_dir / "framework_inventory.json", "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=2)
    except Exception as e:
        print(f"Error writing framework_inventory.json: {e}")

    return primary_framework