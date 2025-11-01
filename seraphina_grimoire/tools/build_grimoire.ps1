<#
.SYNOPSIS
    PowerShell launcher for the Ritual Grimoire Builder.
    Ensures the Python script is executed from the correct directory.
#>

Write-Output "PowerShell Launcher: Building Ritual Grimoire..."

# Get the directory where this script is located
$ScriptDir = Split-Path -Path $MyInvocation.MyCommand.Path -Parent

# Set the location to the script's directory to ensure correct relative paths
Set-Location -Path $ScriptDir

# Define the Python script to run
$PythonScript = "build_grimoire.py"

# Check if the Python script exists
if (-not (Test-Path -Path $PythonScript)) {
    Write-Error "!! FATAL ERROR: Cannot find Python script: $PythonScript"
    exit 1
}

# Execute the Python script
python.exe $PythonScript

Write-Output "✅ Launcher complete."
