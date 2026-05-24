# ─── NYX SOVEREIGN BOOTSTRAPPER v4.0.0 ───
$NyxDir = Join-Path $HOME ".nyx"
Remove-Item -Path $NyxDir -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null

$KernelPath = Join-Path $NyxDir "engine.ps1"

@'
$E = [char]27
function global:nyx {
    [Console]::Write("$E[?1049h")
    while (-not [Console]::KeyAvailable) {
        [Console]::Write("$E[H$E[2J")
        Write-Host "`n  $E[38;2;135;95;255m NYX ENGINE v4.0.0 | DYNAMIC MESH MODE $E[0m"
        Write-Host "  $(Get-Date -f 'yyyy-MM-dd HH:mm:ss')"
        Start-Sleep -Milliseconds 200
    }
    [Console]::ReadKey($true) | Out-Null
    [Console]::Write("$E[?1049l")
}
'@ | Out-File $KernelPath -Encoding utf8

$Profile = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $Profile)) { New-Item -ItemType File -Path $Profile -Force | Out-Null }
$Hook = "`nif (Test-Path '$KernelPath') { . '$KernelPath' }"
if ((Get-Content $Profile -Raw -EA SilentlyContinue) -notlike "*nyx*") { Add-Content $Profile $Hook }

Write-Host "✔ Nyx v4.0.0 Sovereign Kernel Deployed." -ForegroundColor Cyan
