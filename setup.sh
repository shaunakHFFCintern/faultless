#!/bin/bash
# Setup script to create ~/faultlens symbolic link pointing to this repository.
# Idempotent and safe to run multiple times.

# Exit immediately if a command exits with a non-zero status
set -e

# 1. Detect the absolute path of the current repository
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$(cd "$SCRIPT_DIR" && pwd)"
LINK_PATH="$HOME/faultlens"

echo "=== FaultLens Workspace Setup ==="
echo "Repository Path: $REPO_ROOT"
echo "Target Symlink: $LINK_PATH"
echo ""

# 2. Check if the target path ~/faultlens already exists
if [ -e "$LINK_PATH" ] || [ -L "$LINK_PATH" ]; then
    # Resolve the target path of the link cleanly
    if command -v python3 >/dev/null 2>&1; then
        TARGET_PATH=$(python3 -c "import os; print(os.path.realpath(os.path.expanduser('~/faultlens')))")
        REPO_PATH_NORMALIZED=$(python3 -c "import os; print(os.path.realpath('$REPO_ROOT'))")
    else
        # Fallback if python3 is not installed
        if [ -L "$LINK_PATH" ]; then
            TARGET_PATH=$(readlink "$LINK_PATH")
            # Convert to absolute path if it is relative
            if [[ "$TARGET_PATH" != /* ]]; then
                TARGET_PATH="$(cd "$(dirname "$LINK_PATH")" && cd "$(dirname "$TARGET_PATH")" && pwd)/$(basename "$TARGET_PATH")"
            fi
        else
            TARGET_PATH=""
        fi
        REPO_PATH_NORMALIZED="$REPO_ROOT"
    fi

    # Check if target points to this repository
    if [ "$TARGET_PATH" = "$REPO_PATH_NORMALIZED" ]; then
        echo "Success: ~/faultlens already exists and points to this repository ($REPO_PATH_NORMALIZED)."
        exit 0
    else
        echo "Warning: ~/faultlens already exists but points to a different location: '$TARGET_PATH'" >&2
        echo "This repository is located at: '$REPO_PATH_NORMALIZED'" >&2
        echo "To avoid conflicts, the script will not overwrite ~/faultlens automatically." >&2
        echo "Please delete or move ~/faultlens manually if you want to re-point it." >&2
        exit 1
    fi
fi

# 3. Create the symlink
echo "Creating symbolic link $LINK_PATH -> $REPO_ROOT..."
ln -s "$REPO_ROOT" "$LINK_PATH"

# Verify creation
if [ -L "$LINK_PATH" ]; then
    echo "Success: ~/faultlens created successfully."
else
    echo "Error: Failed to create symbolic link." >&2
    exit 1
fi
