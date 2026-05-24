$nyxDir = "$HOME\.nyx"
$bin = "$nyxDir\nyx.exe"

# Setup
New-Item -ItemType Directory -Force "$nyxDir\inbox" | Out-Null

# Compile (Using your local System.Data.SQLite)
csc /target:exe /out:$bin NyxEngine.cs /r:System.Data.SQLite.dll

# Activation
Start-Process $bin -ArgumentList "--daemon" -WindowStyle Hidden
[System.Environment]::SetEnvironmentVariable('Path', "$env:Path;$nyxDir", 'User')

Write-Host "NyxEngine v1.0 Engaged. Type 'nyx' to enter the Sovereign Interface." -ForegroundColor Cyan
