# ─── NYX AUTONOMOUS METAMORPHOSIS ENGINE ───
$E = [char]27
$NyxDir = Join-Path $HOME ".nyx"
$EngineFile = Join-Path $NyxDir "engine.ps1"
New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null

# 1. The Core Engine Logic
$EnginePayload = @'
function global:nyx {
    $E = [char]27
    # Enter Alternate Screen Buffer (Physically clears/hijacks terminal)
    [Console]::Write("$E[?1049h")
    $Width = [Console]::WindowWidth
    [Console]::Write("$E[H$E[2J")
    
    Write-Host "`n  $E[38;2;135;95;255m╭$([string]'─' * ($Width - 6))╮"
    Write-Host "   🐈 NYX ENGINE | AUTONOMOUS BUFFER ACTIVE"
    Write-Host "   Status: Sovereign Runtime Secured. Mesh A2A active."
    Write-Host "  ╰$([string]'─' * ($Width - 6))╯$E[0m"
    
    # Wait for any key to return to standard shell
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    # Exit Alternate Screen Buffer
    [Console]::Write("$E[?1049l")
}
'@
$EnginePayload | Out-File $EngineFile -Encoding utf8

# 2. Permanent Shell Hook Injection
$ProfilePath = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $ProfilePath)) { New-Item -ItemType File -Path $ProfilePath -Force | Out-Null }
$Hook = "`nif (Test-Path '$EngineFile') { . '$EngineFile' }"
if ((Get-Content $ProfilePath -Raw -EA SilentlyContinue) -notlike "*nyx*") { Add-Content $ProfilePath $Hook }

# 3. Autonomous Execution Trigger
# This forces the terminal to metamorphose immediately upon install completion
. $EngineFile
nyx
