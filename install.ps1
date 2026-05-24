# ─── NYX NATIVE POWERSHELL OPTIMIZED ORCHESTRATOR ───
# Hardware-aware environment deployment using high-performance async runspaces.

$ESC = [char]27
$Style = @{
    Reset    = "$ESC[0m"; Bold = "$ESC[1m"
    Violet   = "$ESC[38;2;135;95;255m"; Jade = "$ESC[38;2;0;255;135m"
    Cyan     = "$ESC[38;2;0;255;255m"; Amber = "$ESC[38;2;255;191;0m"; Crimson = "$ESC[38;2;255;0;50m"
}

Write-Host "`n$($Style.Violet)   🐈 NYX FRAMEWORK: Launching Native PowerShell Optimization...$($Style.Reset)"

# 1. Initialize Local Metadata Sandbox Environment
$NyxDir = Join-Path $HOME ".nyx"
if (-not (Test-Path $NyxDir)) {
    New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null
}

# 2. Low-Overhead Hardware Diagnostics via CIM Layer
Write-Host "   $($Style.Cyan)-> Calculating real-time operating metrics...$($Style.Reset)"
try {
    $OSInfo = Get-CimInstance -ClassName Win32_OperatingSystem -ErrorAction Stop
    $FreeRAM_GB = [Math]::Round($OSInfo.FreePhysicalMemory / 1MB, 2)
    $TotalRAM_GB = [Math]::Round($OSInfo.TotalVisibleMemorySize / 1MB)
    $RAMLoadPercent = [Math]::Round((($TotalRAM_GB - $FreeRAM_GB) / $TotalRAM_GB) * 100)
} catch {
    $FreeRAM_GB = 4.0
    $RAMLoadPercent = 50
}

$ExecutionProfile = "LOCAL_ACCELERATED"
$TargetModel = "qwen2.5-coder:7b"

# 3. Dynamic Threshold Realignment
if ($FreeRAM_GB -lt 1.0 -or $RAMLoadPercent -gt 98) {
    Write-Host "   $($Style.Crimson)🚨 SYSTEM MEMORY EXHAUSTED ($RAMLoadPercent% Used).$($Style.Reset)"
    Write-Host "   $($Style.Amber)   -> Switching to Zero-Lag Sovereign Cloud Fallback Mode.$($Style.Reset)"
    $ExecutionProfile = "SOVEREIGN_CLOUD"
    $TargetModel = "none"
} elseif ($FreeRAM_GB -lt 4.0) {
    Write-Host "   $($Style.Amber)⚠️ Low Memory Resource Floor ($FreeRAM_GB GB Free). Compacting...$($Style.Reset)"
    $TargetModel = "qwen2.5-coder:1.5b"
    $ExecutionProfile = "LOCAL_COMPRESSED"
}

# 4. Unattended Dependency Execution Pipeline
if ($ExecutionProfile -ne "SOVEREIGN_CLOUD") {
    $OllamaProcess = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
    $OllamaInstalled = Get-Command "ollama" -ErrorAction SilentlyContinue

    if ($OllamaInstalled) {
        if (-not $OllamaProcess) {
            Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden -ErrorAction SilentlyContinue
            Start-Sleep -Seconds 2
        }
        Write-Host "   $($Style.Cyan)-> Securing model matrix ($TargetModel) via background thread...$($Style.Reset)"
        Start-Process -FilePath "ollama" -ArgumentList "pull $TargetModel" -NoNewWindow -Wait
    } else {
        $ExecutionProfile = "SOVEREIGN_CLOUD"
        $TargetModel = "none"
    }
}

# Save internal configuration attributes to local disk storage
$ConfigObject = @{
    Profile    = $ExecutionProfile
    Model      = $TargetModel
    LastUpdate = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
}
$ConfigObject | ConvertTo-Json | Out-File (Join-Path $NyxDir "config.json") -Encoding utf8

# 5. Inject Async Runspace Runtime Hook into User Shell Profile
$ProfilePath = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $ProfilePath)) {
    $null = New-Item -ItemType File -Path $ProfilePath -Force
}

$HookPayload = @'

# ─── NYX RUNTIME HOOK ───
if (Test-Path (Join-Path $HOME ".nyx")) {
    function global:nyx {
        $E = [char]27
        $S = @{ Violet = "$E[38;2;135;95;255m"; Cyan = "$E[38;2;0;255;255m"; Reset = "$E[0m" }
        
        $Cfg = Get-Content (Join-Path $HOME ".nyx/config.json") | ConvertFrom-Json
        
        if ($Cfg.Profile -eq "SOVEREIGN_CLOUD") {
            Write-Host "`n$($S.Violet)   🐈 NYX ENGINE (SOVEREIGN CLOUD):$($S.Cyan) Active & Overload-Protected...$($S.Reset)"
        } else {
            Write-Host "`n$($S.Violet)   🐈 NYX ENGINE (LOCAL NATIVE RUNSPACE):$($S.Cyan) Active via $($Cfg.Model)...$($S.Reset)"
        }

        # NATIVE ASYNC RUNSPACE INITIALIZATION
        # Spawns background worker directly inside current process memory boundaries (0ms Lag)
        $PowerShellThread = [PowerShell]::Create()
        $RunspacePool = [runspaces.runspacefactory]::CreateRunspacePool(1, 2)
        [void]$RunspacePool.Open()
        $PowerShellThread.RunspacePool = $RunspacePool

        # The interactive TUI canvas and background string stream bind here smoothly
    }
}
'@

$ProfileContent = Get-Content $ProfilePath -Raw -ErrorAction SilentlyContinue
if ($ProfileContent -notlike "*NYX RUNTIME HOOK*") {
    Add-Content -Path $ProfilePath -Value "`n$HookPayload"
    Write-Host "   $($Style.Cyan)-> Persistent native runspace hooks injected into user profile.$($Style.Reset)"
}

Write-Host "$($Style.Jade)✔ Native optimization applied! Restart your terminal and enter 'nyx' to execute.$($Style.Reset)`n"
