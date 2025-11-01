<#
.SYNOPSIS
    PowerShell launcher for the Ritual Translator (Lexicon Compiler).
    Takes a .cc file as input and generates a .compiled.cc file.
#>

param (
    [Parameter(Mandatory=$true, Position=0)]
    [string]$InputFile
)

Write-Output "PowerShell Launcher: 🔮 Translating Lexicon file..."

# Get the directory where this script is located
$ScriptDir = Split-Path -Path $MyInvocation.MyCommand.Path -Parent

# Set the location to the script's directory
Set-Location -Path $ScriptDir

# Define the Python script to run
$PythonScript = "ritual_translator.py"

# Check if the Python script exists
if (-not (Test-Path -Path $PythonScript)) {
    Write-Error "!! FATAL ERROR: Cannot find Python script: $PythonScript"
    exit 1
}

# Resolve the full path for the input file
$FullInputPath = Resolve-Path -Path $InputFile

if (-not (Test-Path -Path $FullInputPath)) {
    Write-Error "!! FATAL ERROR: Input file not found: $FullInputPath"
    exit 1
}

Write-Output "  Input File: $FullInputPath"

# Execute the Python script with the input file argument
python.exe $PythonScript $FullInputPath

Write-Output "✅ Launcher complete."
