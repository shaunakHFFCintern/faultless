# FaultLens

FaultLens is a tool for understanding inherited codebases and identifying faults, risks, and architecture characteristics.

## Standard FaultLens Workspace Setup

To configure and run the `/faultlens` pipeline in this repository (`faultless`), follow these step-by-step instructions:

### 1. Clone the Repository
Clone the repository and enter the directory:
```bash
git clone <repository-url> faultless
cd faultless
```

### 2. Open in Antigravity
Open the `faultless` repository folder in the Antigravity IDE workspace. The `/faultlens` and `/faults` chat commands will be automatically loaded.

### 3. Run the Platform Setup Script
Run the script corresponding to your operating system to align directory mapping:

#### Windows
Run the following command in PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```
*This creates a directory junction at `C:\faultlens` pointing to the repository root.*

#### macOS / Linux
Run the following commands in your terminal:
```bash
chmod +x setup.sh
./setup.sh
```
*This creates a symbolic link at `~/faultlens` pointing to the repository root.*

### 4. Verify Setup using the Test Target
To verify that the pipeline runs successfully, run the slash command against the pre-packaged test target in the Antigravity chat:
```text
/faultlens codebase/test_target
```
*This runs the static collection script, analyzes the code, and automatically generates and opens the compiled `PROJECT_RISK_REGISTER.md` report.*

### 5. Run Against a Custom Local Frontend Codebase
To audit another project, run the slash command pointing to the path of your target codebase:
```text
/faultlens /absolute/path/to/your/frontend/repository
```
*Note: Ensure the target directory contains a valid frontend project with JavaScript, TypeScript, or Vue files and a `package.json` config.*


