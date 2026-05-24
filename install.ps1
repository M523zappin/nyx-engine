# ─── NYX KERNEL V5: AUTONOMOUS SOVEREIGN BOOTSTRAPPER ───
$NyxDir = Join-Path $HOME ".nyx"
Remove-Item -Path $NyxDir -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null
$KernelPath = Join-Path $NyxDir "engine.ps1"

@'
$E = [char]27
function global:nyx {
    [Console]::Write("$E[?1049h") # Enter Alternate Screen
    [Console]::CursorVisible = $false
    while (-not [Console]::KeyAvailable) {
        [Console]::Write("$E[H$E[2J") # Clear Screen
        Write-Host "$E[48;2;30;30;30m$E[38;2;135;95;255m NYX CORE | DYNAMIC UI $E[0m"
        Write-Host " ---------------------------------------"
        Write-Host "  $(Get-Date -f 'yyyy-MM-dd HH:mm:ss') "
        Write-Host " ---------------------------------------"
        Start-Sleep -Milliseconds 250
    }
    [Console]::ReadKey($true) | Out-Null
    [Console]::Write("$E[?1049l") # Exit Alternate Screen
}
nyx
'@ | Out-File $KernelPath -Encoding utf8

# Hardened Profile Injection
$Profile = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $Profile)) { New-Item -ItemType File -Path $Profile -Force | Out-Null }
$Hook = "`nif (Test-Path '$KernelPath') { . '$KernelPath' }"
if ((Get-Content $Profile -Raw -EA SilentlyContinue) -notlike "*nyx*") { Add-Content $Profile $Hook }

Write-Host "✔ Nyx V5 Autonomous Kernel Deployed." -ForegroundColor Cyan
