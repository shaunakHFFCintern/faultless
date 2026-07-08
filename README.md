# FaultLens (v1.5.1)

FaultLens is a tool for understanding inherited frontend codebases and identifying modular dependencies, state relationships, and architectural risks.

---

## 1. Quick Start Guide

Follow these steps to set up and run FaultLens on your local machine.

### Prerequisites:
- **Python 3.10+** (Ensure it is added to your environment `PATH`).
- **Antigravity IDE** (Opened at the root workspace of this repository).

### Setup Flow:

#### macOS
1. **Clone the FaultLens repository**:
   ```bash
   git clone <repository-url> faultless
   cd faultless
   ```
2. **Run the setup script**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   *This creates a symbolic link at `~/faultlens` pointing to the repository root.*
3. **Configure the target repository**:
   Specify the path of the frontend codebase you want to analyze in the config file:
   ```bash
   echo "/Users/username/Desktop/my-project" > proj/agents/docscan/config/target_repo.txt
   ```
4. **Run FaultLens**:
   In the Antigravity chat, trigger the scan command:
   ```text
   /faultlens
   ```

#### Windows (PowerShell)
1. **Clone the FaultLens repository**:
   ```powershell
   git clone <repository-url> faultless
   cd faultless
   ```
2. **Run the setup script**:
   Open PowerShell as Administrator and execute:
   ```powershell
   powershell -ExecutionPolicy Bypass -File setup.ps1
   ```
   *This creates a directory junction at `C:\faultlens` pointing to the repository root.*
3. **Configure the target repository**:
   Specify the path of the frontend codebase you want to analyze in the config file:
   ```powershell
   Set-Content proj/agents/docscan/config/target_repo.txt "C:\Users\Username\Desktop\my-project"
   ```
4. **Run FaultLens**:
   In the Antigravity chat, trigger the scan command:
   ```text
   /faultlens
   ```

---

## 2. Selecting the Repository to Analyze

FaultLens does not scan its own repository. Instead, it reads the target path from the configuration file located at:
`proj/agents/docscan/config/target_repo.txt`

### How to configure:
The file must contain exactly one line pointing to the **absolute path** of the local frontend repository to be scanned.

- **macOS / Linux Configuration**:
  ```bash
  echo "/Users/username/Desktop/my-project" > proj/agents/docscan/config/target_repo.txt
  ```
- **Windows PowerShell Configuration**:
  ```powershell
  Set-Content proj/agents/docscan/config/target_repo.txt "C:\Users\Username\Desktop\my-project"
  ```

---

## 3. Verification & Troubleshooting

Before running `/faultlens`, verify that your configuration is correct to prevent scan failures.

### Checklists:
1. **Confirm target_repo.txt Path**:
   Verify the file contains the correct absolute path to your project.
   - macOS: `cat proj/agents/docscan/config/target_repo.txt`
   - Windows: `Get-Content proj/agents/docscan/config/target_repo.txt`
2. **Ensure the Repository Exists**:
   Ensure that the target folder has been fully cloned and is accessible on your local filesystem.
3. **Verify package.json Presence**:
   Ensure a `package.json` file is present in the root folder of the target path. FaultLens uses this file to discover dependencies and stacks.
4. **Verify Platform Setup**:
   Ensure the platform symlink (`~/faultlens` on macOS or `C:\faultlens` on Windows) is active and targets the root of the cloned `faultless` repository.
