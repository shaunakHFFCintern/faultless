def detect(package_data, file_records):
    technologies = []

    deps = package_data.get("dependencies", {})
    dev_deps = package_data.get("devDependencies", {})
    all_deps = {**deps, **dev_deps}

    # 1. Framework: Vue
    has_vue = "vue" in all_deps
    
    # Fallback to file extension checks
    if not has_vue and file_records:
        has_vue = any(r.get("extension") == ".vue" for r in file_records)

    if has_vue:
        vue_version = all_deps.get("vue", "Unknown")
        technologies.append({
            "name": "Vue",
            "version": vue_version,
            "category": "Frontend Framework",
            "detector": "vue.py"
        })

        # 2. Libraries
        # Pinia
        if "pinia" in all_deps:
            technologies.append({
                "name": "Pinia",
                "version": all_deps.get("pinia", "Unknown"),
                "category": "State Management",
                "detector": "vue.py"
            })

        # Vuex
        if "vuex" in all_deps:
            technologies.append({
                "name": "Vuex",
                "version": all_deps.get("vuex", "Unknown"),
                "category": "State Management",
                "detector": "vue.py"
            })

        # Tailwind CSS
        if "tailwindcss" in all_deps:
            technologies.append({
                "name": "Tailwind",
                "version": all_deps.get("tailwindcss", "Unknown"),
                "category": "Styling",
                "detector": "vue.py"
            })

        # Apollo / GraphQL
        if "@vue/apollo-composable" in all_deps or "apollo-client" in all_deps or "@apollo/client" in all_deps:
            ver = all_deps.get("@vue/apollo-composable", all_deps.get("@apollo/client", "Unknown"))
            technologies.append({
                "name": "Apollo Client",
                "version": ver,
                "category": "Data Fetching",
                "detector": "vue.py"
            })

        if "graphql" in all_deps:
            technologies.append({
                "name": "GraphQL",
                "version": all_deps.get("graphql", "Unknown"),
                "category": "Data Fetching",
                "detector": "vue.py"
            })

    return technologies
