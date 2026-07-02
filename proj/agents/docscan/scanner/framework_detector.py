from pathlib import Path


def detect_framework(repo_path):

    repo = Path(repo_path).expanduser().resolve()

    files = [x.name for x in repo.iterdir()]

    if "hooks.py" in files:
        return "frappe"

    if "package.json" in files:
        return "node"

    if "manage.py" in files:
        return "django"

    if "pyproject.toml" in files:
        return "python"

    return "unknown"