def detect(package_data, file_records):
    technologies = []

    deps = package_data.get("dependencies", {})
    dev_deps = package_data.get("devDependencies", {})
    all_deps = {**deps, **dev_deps}

    # 1. Framework: React / CRA
    has_react = "react" in all_deps or "react-dom" in all_deps
    
    # If no package.json, check file extensions as fallback
    if not has_react and file_records:
        has_react = any(r.get("extension") in {".jsx", ".tsx"} for r in file_records)

    if has_react:
        react_version = all_deps.get("react", "Unknown")
        technologies.append({
            "name": "React",
            "version": react_version,
            "category": "Frontend Framework",
            "detector": "react.py"
        })

        if "react-scripts" in all_deps:
            technologies.append({
                "name": "CRA (Create React App)",
                "version": all_deps.get("react-scripts", "Unknown"),
                "category": "Meta Framework",
                "detector": "react.py"
            })

        # 2. Libraries
        # React Router
        if "react-router" in all_deps or "react-router-dom" in all_deps:
            ver = all_deps.get("react-router-dom", all_deps.get("react-router", "Unknown"))
            technologies.append({
                "name": "React Router",
                "version": ver,
                "category": "Routing",
                "detector": "react.py"
            })

        # Redux
        if "@reduxjs/toolkit" in all_deps or "redux" in all_deps:
            ver = all_deps.get("@reduxjs/toolkit", all_deps.get("redux", "Unknown"))
            technologies.append({
                "name": "Redux",
                "version": ver,
                "category": "State Management",
                "detector": "react.py"
            })

        # MobX
        if "mobx" in all_deps or "mobx-react" in all_deps or "mobx-react-lite" in all_deps:
            ver = all_deps.get("mobx", "Unknown")
            technologies.append({
                "name": "MobX",
                "version": ver,
                "category": "State Management",
                "detector": "react.py"
            })

        # Zustand
        if "zustand" in all_deps:
            technologies.append({
                "name": "Zustand",
                "version": all_deps.get("zustand", "Unknown"),
                "category": "State Management",
                "detector": "react.py"
            })

        # TanStack Query (react-query)
        if "react-query" in all_deps or "@tanstack/react-query" in all_deps:
            ver = all_deps.get("@tanstack/react-query", all_deps.get("react-query", "Unknown"))
            technologies.append({
                "name": "TanStack Query",
                "version": ver,
                "category": "Data Fetching",
                "detector": "react.py"
            })

        # Styled Components
        if "styled-components" in all_deps:
            technologies.append({
                "name": "Styled Components",
                "version": all_deps.get("styled-components", "Unknown"),
                "category": "Styling",
                "detector": "react.py"
            })

        # Tailwind CSS
        if "tailwindcss" in all_deps:
            technologies.append({
                "name": "Tailwind",
                "version": all_deps.get("tailwindcss", "Unknown"),
                "category": "Styling",
                "detector": "react.py"
            })

        # Form Validation libraries
        if "react-hook-form" in all_deps:
            technologies.append({
                "name": "React Hook Form",
                "version": all_deps.get("react-hook-form", "Unknown"),
                "category": "Forms",
                "detector": "react.py"
            })

        if "formik" in all_deps:
            technologies.append({
                "name": "Formik",
                "version": all_deps.get("formik", "Unknown"),
                "category": "Forms",
                "detector": "react.py"
            })

        if "zod" in all_deps:
            technologies.append({
                "name": "Zod",
                "version": all_deps.get("zod", "Unknown"),
                "category": "Validation",
                "detector": "react.py"
            })

        if "yup" in all_deps:
            technologies.append({
                "name": "Yup",
                "version": all_deps.get("yup", "Unknown"),
                "category": "Validation",
                "detector": "react.py"
            })

    return technologies
