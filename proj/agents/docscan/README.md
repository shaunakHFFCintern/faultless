# DocScan

Purpose

Understand inherited codebases quickly.

Command

/docscan

Outputs

- Executive Summary
- Architecture
- Modules
- Data Flow
- APIs
- Database
- Dependencies
- Function Registry
- Risk Map
- Developer Guide

Success Criteria

A developer should understand the project in under 30 minutes.

Current Status

Setup Complete

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


