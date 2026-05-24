# ─── NYX BUILD & MAPPING SCRIPT ───
$NyxRoot = Join-Path $HOME ".nyx"
New-Item -ItemType Directory -Path $NyxRoot -Force | Out-Null

# Copy kernel to system-local path
Copy-Item "engine.ps1" -Destination (Join-Path $NyxRoot "engine.ps1") -Force

# Create the binary wrapper
$Wrapper = 'powershell.exe -ExecutionPolicy Bypass -File "$HOME\.nyx\engine.ps1"'
$Wrapper | Out-File (Join-Path $NyxRoot "nyx.bat") -Encoding ascii

Write-Host "✔ Build Complete. Nyx Kernel v7 deployed to $NyxRoot" -ForegroundColor Green
