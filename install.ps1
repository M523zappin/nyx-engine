$NyxRoot = Join-Path $HOME ".nyx"
if (!(Test-Path $NyxRoot)) { New-Item -ItemType Directory -Path $NyxRoot | Out-Null }

# Compile the Daemon and Client
csc /target:exe /out:"$NyxRoot\nyx-daemon.exe" "$NyxRoot\NyxKernel.cs"
csc /target:exe /out:"$NyxRoot\nyx.exe" "$NyxRoot\nyx.cs"

# Set up the background startup
# In a production environment, you would use a Task Scheduler or Windows Service
Write-Host "✔ Nyx Evolved. Run 'nyx-daemon' in background, then use 'nyx <command>'." -ForegroundColor Green
