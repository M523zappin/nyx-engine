# ─── NYX KERNEL v7.0 | SOVEREIGN ARCHITECTURE ───
[CmdletBinding()]
param()

$E = [char]27
[Console]::Write("$E[?1049h")
[Console]::CursorVisible = $false

try {
    # Initialize the Render Engine
    while (-not [Console]::KeyAvailable) {
        # Buffer Clear & Reset
        [Console]::Write("$E[H$E[2J")
        
        # State Matrix
        $Time = Get-Date -f "HH:mm:ss"
        Write-Host "$E[48;2;30;30;30m$E[38;2;135;95;255m NYX ENGINE [KERNEL v7] $E[K"
        Write-Host " ---------------------------------------"
        Write-Host "  TIME: $Time"
        Write-Host "  STATE: Sovereign Execution Pool Active"
        Write-Host " ---------------------------------------"
        Write-Host "`n [!] Waiting for Input..." -ForegroundColor DarkGray
        
        # CPU-Efficient Pulse
        Start-Sleep -Milliseconds 250
    }
} finally {
    # Cleanup & Restore
    [Console]::CursorVisible = $true
    [Console]::Write("$E[?1049l")
}
