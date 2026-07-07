from pathlib import Path

def detect(package_data, file_records):
    technologies = []

    deps = package_data.get("dependencies", {})
    dev_deps = package_data.get("devDependencies", {})
    all_deps = {**deps, **dev_deps}

    # 1. Next.js
    if "next" in all_deps:
        technologies.append({
            "name": "Next.js",
            "version": all_deps.get("next", "Unknown"),
            "category": "Meta Framework",
            "detector": "nextjs.py"
        })

    # 2. Nuxt
    if "nuxt" in all_deps:
        technologies.append({
            "name": "Nuxt",
            "version": all_deps.get("nuxt", "Unknown"),
            "category": "Meta Framework",
            "detector": "nextjs.py"
        })

    # 3. Vite
    if "vite" in all_deps:
        technologies.append({
            "name": "Vite",
            "version": all_deps.get("vite", "Unknown"),
            "category": "Build Tool",
            "detector": "nextjs.py"
        })

    # 4. Testing Libraries
    if "jest" in all_deps:
        technologies.append({
            "name": "Jest",
            "version": all_deps.get("jest", "Unknown"),
            "category": "Testing",
            "detector": "nextjs.py"
        })

    if "vitest" in all_deps:
        technologies.append({
            "name": "Vitest",
            "version": all_deps.get("vitest", "Unknown"),
            "category": "Testing",
            "detector": "nextjs.py"
        })

    if "cypress" in all_deps:
        technologies.append({
            "name": "Cypress",
            "version": all_deps.get("cypress", "Unknown"),
            "category": "Testing",
            "detector": "nextjs.py"
        })

    if "playwright" in all_deps or "@playwright/test" in all_deps:
        ver = all_deps.get("@playwright/test", all_deps.get("playwright", "Unknown"))
        technologies.append({
            "name": "Playwright",
            "version": ver,
            "category": "Testing",
            "detector": "nextjs.py"
        })

    # 5. Package Manager Detection via files
    if file_records:
        # Check parent folder lockfiles
        # Note: file_records contains relative paths
        has_pnpm = any(r.get("path") == "pnpm-lock.yaml" for r in file_records)
        has_yarn = any(r.get("path") == "yarn.lock" for r in file_records)
        has_npm = any(r.get("path") == "package-lock.json" for r in file_records)

        if has_pnpm:
            technologies.append({
                "name": "pnpm",
                "version": "Observed from lockfile",
                "category": "Package Manager",
                "detector": "nextjs.py"
            })
        elif has_yarn:
            technologies.append({
                "name": "Yarn",
                "version": "Observed from lockfile",
                "category": "Package Manager",
                "detector": "nextjs.py"
            })
        elif has_npm:
            technologies.append({
                "name": "npm",
                "version": "Observed from lockfile",
                "category": "Package Manager",
                "detector": "nextjs.py"
            })

    return technologies
