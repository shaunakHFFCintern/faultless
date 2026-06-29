from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def write_discovery(target, framework, result):

    output = BASE_DIR / "outputs" / "DISCOVERY.md"

    with open(output, "w", encoding="utf-8") as f:

        f.write("# Discovery\n\n")

        f.write(f"Target:\n{target}\n\n")

        f.write(f"Framework:\n{framework}\n\n")

        f.write("## Folders\n")

        for folder in result["folders"]:
            f.write(f"- {folder}\n")

        f.write("\n## Files\n")

        for file in result["files"]:
            f.write(f"- {file}\n")

    return output
def write_exec_summary(target, framework, result):

    output = BASE_DIR / "outputs" / "EXEC_SUMMARY.md"

    with open(output, "w", encoding="utf-8") as f:

        f.write("# Executive Summary\n\n")

        f.write("## Repository\n")
        f.write(f"{target}\n\n")

        f.write("## Framework\n")
        f.write(f"{framework}\n\n")

        f.write("## Executive View\n\n")

        f.write(
            f"This repository contains "
            f"{len(result['folders'])} top-level modules "
            f"and "
            f"{len(result['files'])} root files.\n\n"
        )

        f.write("## Core Areas\n\n")

        for folder in result["folders"]:
            f.write(f"- {folder}\n")

        f.write("\n## Immediate Developer Focus\n\n")

        f.write(
            "- Understand architecture\n"
        )

        f.write(
            "- Locate business logic\n"
        )

        f.write(
            "- Identify extension points\n"
        )

        f.write(
            "- Avoid modifying generated assets\n"
        )

    return output