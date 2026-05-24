# Nyx-Cat Bootstrap
$NyxDir = "$HOME/.nyx"
if (!(Test-Path $NyxDir)) { 
    New-Item -ItemType Directory -Path $NyxDir 
}

# Sync local SOUL to runtime
Copy-Item -Path ".\Soul.md" -Destination "$NyxDir\SOUL.md" -Force

Write-Host "Nyx-Cat Initialized. Entering Sovereign State." -ForegroundColor Green
python NyxEngine.py
