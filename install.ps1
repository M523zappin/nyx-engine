# ─── NYX KERNEL v2.0.0 | SOVEREIGN VIEWPORT ENGINE ───
$E = [char]27

function global:nyx {
    # Enter Alternate Screen Buffer (Physically separates from shell history)
    [Console]::Write("$E[?1049h")
    
    # Initialization of the Viewport
    $W = [Console]::WindowWidth
    $H = [Console]::WindowHeight
    
    # State-ful render loop (Preventing static output)
    [Console]::Write("$E[H$E[2J")
    
    # Render Frame
    $Border = [string]'─' * ($W - 6)
    Write-Host "`n  $E[38;2;135;95;255m╭$Border╮"
    Write-Host "   🐈 NYX ENGINE | OPENCODE INTERFACE | KERNEL v2.0.0"
    Write-Host "   SYSTEM STATUS: MONITORING .NET RUNSPACE POOLS"
    Write-Host "   RUNTIME: $([System.Diagnostics.Process]::GetCurrentProcess().Id)"
    Write-Host "  ╰$Border╯$E[0m`n"
    Write-Host "   > Awaiting Agent-to-Agent (A2A) handshake..."

    # Input capture (Non-blocking loop)
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    
    # Exit Alternate Screen Buffer (Restores original shell intact)
    [Console]::Write("$E[?1049l")
}
