# ─── NYX AUTONOMOUS INSTALLER FRAMEWORK ───
# Clean, lightweight open-source bootstrapper for the nyx-engine terminal ecosystem.

$ESC = [char]27
$Style = @{
    Reset = "$ESC[0m"; Bold = "$ESC[1m"
    Violet = "$ESC[38;2;135;95;255m"; Jade = "$ESC[38;2;0;255;135m"
    Cyan  = "$ESC[38;2;0;255;255m"
}

Write-Host "`n$($Style.Violet)🐈 NYX FRAMEWORK: Initializing open-source terminal deployment...$($Style.Reset)"

# 1. Establish the clean, hidden environment vault directories
$NyxDir = Join-Path $HOME ".nyx"
if (-not (Test-Path $NyxDir)) {
    New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null
    Write-Host "   -> Created secure localized metadata container at: $NyxDir"
}

# 2. Target the persistent user profile path
$ProfilePath = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $ProfilePath)) {
    $null = New-Item -ItemType File -Path $ProfilePath -Force
}

# 3. Define the Global Startup Alias Configuration block
$HookPayload = @"

# ─── NYX RUNTIME HOOK ───
# Automated zero-credit local agent alias initialization
if (Test-Path '$NyxDir') {
    # This automatically intercepts terminal execution when 'nyx' is called
    function global:nyx {
        Write-Host "`n$($Style.Violet)   🐈 NYX ENGINE:$($Style.Cyan) Standing by to prowl codebase matrix...$($Style.Reset)"
        # The core visual layout and local model connection loops call sequentially here
    }
}
"@

# 4. Inject the hook safely if it does not already exist in the profile
$ProfileContent = Get-Content $ProfilePath -Raw -ErrorAction SilentlyContinue
if ($ProfileContent -notlike "*NYX RUNTIME HOOK*") {
    Add-Content -Path $ProfilePath -Value "`n$HookPayload"
    Write-Host "   -> Successfully injected persistent startup aliases into user shell profile."
}

Write-Host "$($Style.Jade)✔ Deployment finalized. Restart your terminal window and type 'nyx' to start modeling.$($Style.Reset)`n"
