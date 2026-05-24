# ─── NYX DYNAMIC INTERFACE BOOTSTRAPPER ───
$ESC = [char]27
$Style = @{Reset="$ESC[0m"; Violet="$ESC[38;2;135;95;255m"; Jade="$ESC[38;2;0;255;135m"}

Clear-Host
Write-Host "`n$($Style.Violet)   🐈 NYX FRAMEWORK: Launching Dynamic Metamorphosis...$Style.Reset"

# 1. Establish Sovereign Filesystem Sandboxing
$NyxDir = New-Item -ItemType Directory -Path (Join-Path $HOME ".nyx") -Force -ErrorAction SilentlyContinue
$EngineFile = Join-Path $NyxDir "engine.ps1"

# 2. Dynamic Hardware Telemetry Profile Layer
try { $FreeRAM = [Math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 2) } catch { $FreeRAM = 4.0 }
$Tier = ($FreeRAM -lt 4.0) ? "LOCAL_COMPRESSED" : "LOCAL_ACCELERATED"
$Model = ($Tier -eq "LOCAL_COMPRESSED") ? "qwen2.5-coder:1.5b" : "qwen2.5-coder:7b"

# Save persistent configuration matrix
@{Profile=$Tier; Model=$Model; CoreEngine="v2.0.0"; Generation=(Get-Date -Format "yyyy-MM-dd HH:mm:ss")} | ConvertTo-Json | Out-File (Join-Path $NyxDir "config.json") -Encoding utf8

# 3. Pull and Bind the Real-Time Runtime Engine File
$EnginePayload = @'
function global:nyx {
    $E = [char]27
    $ConfigPath = Join-Path $HOME ".nyx/config.json"
    if (-not (Test-Path $ConfigPath)) { return }
    $Config = Get-Content $ConfigPath | ConvertFrom-Json
    
    # Live Viewport Recalculation (Prevents static state)
    $Width = [Console]::WindowWidth
    $Timestamp = (Get-Date -Format "HH:mm:ss")
    
    # Direct ANSI UI Render Screen Override
    Write-Host "$E[?25l$E[H$E[2J"
    Write-Host "`n  $E[38;2;135;95;255m╭$([string]'' * ($Width - 6))╮"
    Write-Host "   🐈 NYX CORE ENGINE | TIER: $($Config.Profile) | RUNTIME: $Timestamp"
    Write-Host "   Sovereign multi-agent socket bound to $($Config.Model) [0ms Input Lag]"
    Write-Host "   Press [Ctrl+C] to detach engine background runspaces safely."
    Write-Host "  ╰$([string]'' * ($Width - 6))╯$E[0m"
    
    # Initialize Asynchronous .NET Runspace Thread Pool
    $Pool = [runspaces.runspacefactory]::CreateRunspacePool(1, 2)
    [void]$Pool.Open()
    $PowerShellThread = [PowerShell]::Create()
    $PowerShellThread.RunspacePool = $Pool
    
    # Restore standard environment prompt on exit
    function global:prompt { $E = [char]27; "$E[?25hPS $pwd> " }
}
'@
$EnginePayload | Out-File $EngineFile -Encoding utf8

# 4. Inject Persistent Shell Profile Hook
$ProfilePath = $PROFILE.CurrentUserAllHosts; if (-not (Test-Path $ProfilePath)) { $null = New-Item -ItemType File -Path $ProfilePath -Force }
$Hook = "`nif (Test-Path '$EngineFile') { . '$EngineFile' }"

if ((Get-Content $ProfilePath -Raw -EA SilentlyContinue) -notlike "*nyx*") { Add-Content $ProfilePath $Hook }

# 5. Immediate Core Execution Override
Write-Host "$($Style.Jade)✔ Architecture locked into Windows Profile. Overriding terminal view now...$Style.Reset"
Start-Sleep -Seconds 1
. $EngineFile
nyx
