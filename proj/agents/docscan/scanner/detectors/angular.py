def detect(package_data, file_records):
    technologies = []

    deps = package_data.get("dependencies", {})
    dev_deps = package_data.get("devDependencies", {})
    all_deps = {**deps, **dev_deps}

    # 1. Framework: Angular
    has_angular = "@angular/core" in all_deps
    
    # Fallback checks
    if not has_angular and file_records:
        has_angular = any(".component." in r.get("path", "") for r in file_records)

    if has_angular:
        angular_version = all_deps.get("@angular/core", "Unknown")
        technologies.append({
            "name": "Angular",
            "version": angular_version,
            "category": "Frontend Framework",
            "detector": "angular.py"
        })

        if "tailwindcss" in all_deps:
            technologies.append({
                "name": "Tailwind",
                "version": all_deps.get("tailwindcss", "Unknown"),
                "category": "Styling",
                "detector": "angular.py"
            })

    return technologies
