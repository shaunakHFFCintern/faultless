# FaultLens

FaultLens is a tool for understanding inherited codebases and identifying faults, risks, and architecture characteristics.

## Standard FaultLens Workspace Setup

To configure a standard local workspace, developers should run the onboarding script from the root of the repository:

```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```

After setup:
- `C:\faultlens` will always point to the repository root.
- Internal tooling and Antigravity prompts can safely reference `C:\faultlens`.
- This creates a consistent environment across all developer machines.
