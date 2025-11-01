# Canon Lock - PowerShell One-Liner for Windows
# Usage: .\canon-lock.ps1 [fix|validate|test|all]

param(
    [Parameter(Position=0)]
    [ValidateSet('fix', 'validate', 'test', 'all', 'help')]
    [string]$Command = 'all'
)

$ErrorActionPreference = "Stop"
$RosettaPath = "CODECRAFT_ROSETTA_STONE.md"

function Show-Help {
    Write-Host ""
    Write-Host "🔒 CodeCraft Canon Lock - PowerShell Edition" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage: .\canon-lock.ps1 [command]" -ForegroundColor White
    Write-Host ""
    Write-Host "Commands:" -ForegroundColor Yellow
    Write-Host "  fix       - Update integrity hash" -ForegroundColor White
    Write-Host "  validate  - Verify hash matches" -ForegroundColor White
    Write-Host "  test      - Run pytest suite" -ForegroundColor White
    Write-Host "  all       - Run all checks (default)" -ForegroundColor White
    Write-Host "  help      - Show this help" -ForegroundColor White
    Write-Host ""
}

function Invoke-Fix {
    Write-Host "⚙️  Computing canonical hash..." -ForegroundColor Yellow
    python -m scripts.fix_integrity_hash $RosettaPath
    if ($LASTEXITCODE -ne 0) { throw "Fixer failed!" }
}

function Invoke-Validate {
    Write-Host "✅ Validating Rosetta Stone integrity..." -ForegroundColor Green
    python -m scripts.lost_validate $RosettaPath
    if ($LASTEXITCODE -ne 0) { throw "Validator failed!" }
}

function Invoke-Test {
    Write-Host "🍰 Running pytest suite..." -ForegroundColor Magenta
    pytest -q tests/test_rosetta_integrity.py
    if ($LASTEXITCODE -ne 0) { throw "Tests failed!" }
}

function Invoke-All {
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "🔒 CANON LOCK: Running All Checks" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host ""
    
    Invoke-Fix
    Write-Host ""
    Invoke-Validate
    Write-Host ""
    Invoke-Test
    
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
    Write-Host "🎉 CANON LOCK: ALL CHECKS PASSED! 🎉" -ForegroundColor Green
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
    Write-Host "  📜 Rosetta Stone cryptographically sealed" -ForegroundColor White
    Write-Host "  ✨ The Forge stands eternal!" -ForegroundColor White
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
    Write-Host ""
}

# Main execution
try {
    switch ($Command) {
        'fix' { Invoke-Fix }
        'validate' { Invoke-Validate }
        'test' { Invoke-Test }
        'all' { Invoke-All }
        'help' { Show-Help }
    }
} catch {
    Write-Host ""
    Write-Host "❌ ERROR: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    exit 1
}
