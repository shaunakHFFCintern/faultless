# Setup script to create C:\faultlens junction pointing to this repository.
# Idempotent and safe to run multiple times.

# Ensure errors are caught properly
$ErrorActionPreference = "Stop"

# 1. Detect the absolute path of the current repository automatically using the location of setup.ps1
$ScriptPath = $PSScriptRoot
if ([string]::IsNullOrEmpty($ScriptPath)) {
    $ScriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
}
$RepoPath = [System.IO.Path]::GetFullPath($ScriptPath)
$JunctionPath = "C:\faultlens"

Write-Host "=== FaultLens Workspace Setup ==="
Write-Host "Repository Path: $RepoPath"
Write-Host "Target Junction: $JunctionPath"
Write-Host ""

# 2. Check if the target path C:\faultlens already exists
if (Test-Path -Path $JunctionPath) {
    # Get the details of the existing file/folder
    $item = Get-Item -Path $JunctionPath -ErrorAction SilentlyContinue
    
    # Check if the existing item is a Reparse Point (Junction or Symbolic Link)
    $isReparsePoint = $item -and ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint)
    
    if ($isReparsePoint) {
        # Retrieve the target path of the junction/symbolic link
        $target = $item.Target
        
        # Handle cases where Target is a collection (e.g. in some PowerShell versions)
        if ($target -is [System.Collections.IEnumerable] -and $target -isnot [string]) {
            $target = $target | Select-Object -First 1
        }
        
        if ($target) {
            # Normalize paths to resolve relative paths and trailing slashes
            $normalizedTarget = [System.IO.Path]::GetFullPath($target).TrimEnd('\')
            $normalizedRepo = [System.IO.Path]::GetFullPath($RepoPath).TrimEnd('\')
            
            # If the junction already points to this repository, print success and exit
            if ($normalizedTarget -ieq $normalizedRepo) {
                Write-Host "Success: C:\faultlens already exists and points to this repository ($normalizedRepo)." -ForegroundColor Green
                exit 0
            } else {
                # If it points to a different repository or location, warn and exit
                Write-Warning "C:\faultlens already exists but points to a different location: '$normalizedTarget'"
                Write-Warning "This repository is located at: '$normalizedRepo'"
                Write-Warning "To avoid conflicts, the script will not overwrite C:\faultlens automatically."
                Write-Warning "Please delete C:\faultlens manually if you want to re-point it."
                exit 1
            }
        } else {
            Write-Warning "C:\faultlens exists as a link, but its target path could not be determined."
            exit 1
        }
    } else {
        # The path exists but is a standard directory or file
        Write-Warning "C:\faultlens already exists as a normal folder or file, not a junction."
        Write-Warning "Please manually inspect or remove C:\faultlens before running this script."
        exit 1
    }
}

# 3. Create the Windows Junction using cmd /c mklink /J
Write-Host "Creating directory junction C:\faultlens -> $RepoPath..."
try {
    # mklink is a CMD built-in command, so we execute it via cmd /c
    $output = cmd /c mklink /J "$JunctionPath" "$RepoPath" 2>&1
    
    # Verify creation succeeded by checking the path again
    if (Test-Path -Path $JunctionPath) {
        Write-Host "Success: $output" -ForegroundColor Green
        Write-Host "Standard local alias C:\faultlens created successfully." -ForegroundColor Green
    } else {
        throw "Junction creation reported success but path does not exist. cmd output: $output"
    }
} catch {
    Write-Error "Failed to create directory junction. Error detail: $_"
    exit 1
}
