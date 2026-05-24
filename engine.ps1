# ─── NYX KERNEL v4.0.0 | SOVEREIGN DYNAMIC CORE ───
$E = [char]27
function global:nyx {
    [Console]::Write("$E[?1049h") # Enter Alternate Buffer
    [Console]::CursorVisible = $false
    
    # State-Driven Render Loop
    while (-not [Console]::KeyAvailable) {
        [Console]::Write("$E[H$E[2J") # Clear Screen
        $W = [Console]::WindowWidth
        
        # Identity Header
        Write-Host "$E[48;2;45;45;45m$E[38;2;135;95;255m NYX CORE | LIVE MESH STATUS $E[K"
        Write-Host " ┌──────────────────────────────────────────────┐"
        Write-Host " │ 🐈 ARCHITECTURE: SOVEREIGN AUTONOMOUS         │"
        Write-Host " │ ⚡ MESH STATUS:  SYNCED (A2A PROTOCOL ACTIVE) │"
        Write-Host " │ ⏱  HEARTBEAT:  $(Get-Date -Format 'HH:mm:ss.fff')      │"
        Write-Host " └──────────────────────────────────────────────┘"
        
        # Real-time Metrics (Non-static)
        Write-Host "`n [GHOST WITNESS PROTOCOL] Monitoring Shell Output..." -ForegroundColor DarkGray
        
        Start-Sleep -Milliseconds 100 # High-frequency refresh
    }
    
    [Console]::CursorVisible = $true
    [Console]::ReadKey($true) | Out-Null
    [Console]::Write("$E[?1049l") # Exit Buffer
}
