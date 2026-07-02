# FaultLens

FaultLens is a tool for understanding inherited codebases and identifying faults, risks, and architecture characteristics.

## Standard FaultLens Workspace Setup

To configure a standard local workspace, run the onboarding script from the root of the repository depending on your platform:

### Windows
Run the following command in PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```
After setup:
- `C:\faultlens` will point to the repository root.
- Internal tooling and Antigravity prompts can safely reference `C:\faultlens`.

### macOS / Linux
Run the following commands in the terminal:
```bash
chmod +x setup.sh
./setup.sh
```
After setup:
- `~/faultlens` will point to the repository root (resolving to `/Users/<user>/faultlens` on macOS or `/home/<user>/faultlens` on Linux).
- Internal tooling and Antigravity prompts can safely reference `~/faultlens` or their platform equivalents.

This creates a consistent environment across all developer machines.

