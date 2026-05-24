$nyxDir = "$HOME\.nyx"
New-Item -ItemType Directory -Force "$nyxDir\inbox" | Out-Null
New-Item -ItemType Directory -Force "$nyxDir\outbox" | Out-Null

Write-Host "Synthesizing Nyx-Cat Binary..." -ForegroundColor Cyan
csc /target:exe /out:"$nyxDir\nyx.exe" NyxEngine.cs /r:System.Data.SQLite.dll

if (-not [System.Environment]::GetEnvironmentVariable('Path', 'User').Contains($nyxDir)) {
    [System.Environment]::SetEnvironmentVariable('Path', "$([System.Environment]::GetEnvironmentVariable('Path', 'User'));$nyxDir", 'User')
}
Write-Host "Nyx-Cat Sovereign Intelligence Engaged." -ForegroundColor Green
