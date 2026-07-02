from pathlib import Path


def load_repository(repo_path):

    repo = Path(repo_path).expanduser().resolve()

    if not repo.exists():
        raise Exception(f"Repository not found:\n{repo}")

    folders = []
    files = []

    for item in repo.iterdir():

        if item.is_dir():
            folders.append(item.name)

        else:
            files.append(item.name)

    return {
        "folders": sorted(folders),
        "files": sorted(files)
    }