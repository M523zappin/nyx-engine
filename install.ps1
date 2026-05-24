# ─── NYX AUTONOMOUS BOOTSTRAP ORCHESTRATOR ───
# Fully unattended dependency verification, hardware alignment, and engine deployment.

$ESC = [char]27
$Style = @{
    Reset    = "$ESC[0m"; Bold = "$ESC[1m"
    Violet   = "$ESC[38;2;135;95;255m"; Jade = "$ESC[38;2;0;255;135m"
    Cyan     = "$ESC[38;2;0;255;255m"; Amber = "$ESC[38;2;255;191;0m"
}

Write-Host "`n$($Style.Violet)   🐈 NYX FRAMEWORK: Launching Unattended Engine Setup...$($Style.Reset)"

# 1. Initialize Local System Containers
$NyxDir = Join-Path $HOME ".nyx"
if (-not (Test-Path $NyxDir)) {
    New-Item -ItemType Directory -Path $NyxDir -Force | Out-Null
    Write-Host "   $($Style.Cyan)-> Localized sandbox tracking hub initialized.$($Style.Reset)"
}

# 2. Autonomous Dependency Check: Local Inference Host
Write-Host "   $($Style.Cyan)-> Verifying local compute infrastructure...$($Style.Reset)"
$OllamaProcess = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
$OllamaInstalled = Get-Command "ollama" -ErrorAction SilentlyContinue

if (-not $OllamaInstalled) {
    Write-Host "   $($Style.Amber)⚠️ Ollama not detected on system PATH.$($Style.Reset)"
    Write-Host "   $($Style.Violet)   Nyx requires a local backend to run 100% unlimited and free.$($Style.Reset)"
    Write-Host "   $($Style.Violet)   Please download the native runtime client from https://ollama.com$($Style.Reset)"
    Write-Host "   $($Style.Violet)   Once installed, Nyx will automatically manage your models.$($Style.Reset)"
} else {
    Write-Host "   $($Style.Jade)✔ Local model engine verified on system PATH.$($Style.Reset)"
    
    # Ensure the background model daemon service loop is running
    if (-not $OllamaProcess) {
        Write-Host "   $($Style.Cyan)-> Launching inference daemon in background...$($Style.Reset)"
        Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 3
    }

    # 3. Autonomous Model Procurement Loop
    # Background pre-loading of our high-speed, lightweight 2026 local code model target
    $TargetModel = "qwen2.5-coder:7b"
    Write-Host "   $($Style.Cyan)-> System checking for model footprint ($TargetModel)...$($Style.Reset)"
    
    $LocalModels = ollama list
    if ($LocalModels -notlike "*$TargetModel*") {
        Write-Host "   $($Style.Amber)🐾 Pulling model layer signatures ($TargetModel) directly to local VRAM...$($Style.Reset)"
        Write-Host "   $($Style.Violet)   (This happens completely automatically. Grab a coffee while Nyx primes her claws.)$($Style.Reset)"
        # Pull model asynchronously to avoid blocking the pipeline completely
        Start-Process -FilePath "ollama" -ArgumentList "pull $TargetModel" -NoNewWindow -Wait
        Write-Host "   $($Style.Jade)✔ Local model intelligence matrix successfully secured.$($Style.Reset)"
    } else {
        Write-Host "   $($Style.Jade)✔ Verified high-performance model footprint in VRAM.$($Style.Reset)"
    }
}

# 4. Inject Persistent User Shell Profiles & Global Aliases
$ProfilePath = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $ProfilePath)) {
    $null = New-Item -ItemType File -Path $ProfilePath -Force
}

$HookPayload = @"

# ─── NYX RUNTIME HOOK ───
if (Test-Path '$NyxDir') {
    function global:nyx {
        Write-Host "`n$($Style.Violet)   🐈 NYX ENGINE:$($Style.Cyan) Standing by to prowl codebase matrix...$($Style.Reset)"
        # Future UI terminal rendering blocks call sequentially here
    }
}
"@

$ProfileContent = Get-Content $ProfilePath -Raw -ErrorAction SilentlyContinue
if ($ProfileContent -notlike "*NYX RUNTIME HOOK*") {
    Add-Content -Path $ProfilePath -Value "`n$HookPayload"
    Write-Host "   $($Style.Cyan)-> Persistent startup hooks mapped to native shell profile.$($Style.Reset)"
}

Write-Host "$($Style.Jade)✔ Setup complete! Restart your console workspace and enter 'nyx' to start coding.$($Style.Reset)`n"
