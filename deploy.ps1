# Nyx-Cat Deployment Script
$NyxDir = "$HOME/.nyx"
if (!(Test-Path $NyxDir)) { New-Item -ItemType Directory -Path $NyxDir }

# Link SOUL.md to the active runtime
Copy-Item -Path ".\Soul.md" -Destination "$NyxDir\SOUL.md" -Force

Write-Host "Sovereign Intelligence Initialized." -ForegroundColor Cyan
python NyxEngine.py
