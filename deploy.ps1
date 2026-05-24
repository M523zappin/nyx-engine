$path = "$HOME\.nyx"
Write-Host "--- Initializing Nyx Sovereign Intelligence ---" -ForegroundColor Cyan

# 1. Workspace
New-Item -ItemType Directory -Force "$path\inbox" | Out-Null
New-Item -ItemType Directory -Force "$path\outbox" | Out-Null

# 2. Compilation
Write-Host "Synthesizing Binaries..." -ForegroundColor Yellow
csc /target:exe /out:"$path\nyx-daemon.exe" NyxKernel.cs RegistryManager.cs /r:System.Data.SQLite.dll
csc /target:exe /out:"$path\nyx.exe" nyx.cs

# 3. Environment Integration
$envPath = [System.Environment]::GetEnvironmentVariable('Path', 'User')
if (-not $envPath.Contains($path)) {
    [System.Environment]::SetEnvironmentVariable('Path', "$envPath;$path", 'User')
}

# 4. Instant Engagement
Write-Host "Engaging Sovereign Execution Pool..." -ForegroundColor Green
Start-Process "$path\nyx-daemon.exe" -WindowStyle Hidden
Write-Host "Nyx is now active. Launching interface..." -ForegroundColor Green
Start-Process "$path\nyx.exe"
