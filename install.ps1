# ─── NYX V6 | SOVEREIGN BOOTSTRAPPER ───
$NyxDir = Join-Path $HOME ".nyx"
New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null
$Kernel = Join-Path $NyxDir "engine.ps1"

# Writing the High-Fidelity UI Engine
@'
$E = [char]27
function global:nyx {
    [Console]::Write("$E[?1049h")
    [Console]::CursorVisible = $false
    $W = [Console]::WindowWidth
    
    while (-not [Console]::KeyAvailable) {
        # Frame Rendering
        [Console]::Write("$E[H$E[2J")
        Write-Host "$E[48;2;30;30;30m$E[38;2;135;95;255m NYX 🐈 | SOVEREIGN TERMINAL ENGINE $E[K"
        Write-Host "$E[38;2;135;95;255m" -NoNewline
        Write-Host ("─" * $W)
        Write-Host " STATUS:    [CONNECTED]"
        Write-Host " MESH:      [A2A ACTIVE]"
        Write-Host " CPU LOAD:  $((Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue.ToString('F0'))%"
        Write-Host "`n [READY FOR COMMANDS...]"
        
        Start-Sleep -Milliseconds 100
    }
    [Console]::CursorVisible = $true
    [Console]::Write("$E[?1049l")
}
'@ | Out-File $Kernel -Encoding utf8

# Hard Hook Injection
$Profile = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path (Split-Path $Profile))) { New-Item -ItemType Directory -Path (Split-Path $Profile) -Force | Out-Null }
$Hook = "`n. '$Kernel'; nyx"
if ((Get-Content $Profile -Raw -EA SilentlyContinue) -notlike "*nyx*") { Add-Content $Profile $Hook }
Write-Host "✔ Nyx Engine V6 deployed. Terminal UI active." -ForegroundColor Green
