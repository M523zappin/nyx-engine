# ─── NYX MICRO-BOOTSTRAPPER ───
$E = [char]27; $S = @{V="$E[38;2;135;95;255m";J="$E[38;2;0;255;135m";C="$E[38;2;0;255;255m";R="$E[0m"}
Write-Host "`n$($S.V)🐈 NYX ENGINE: Securing sovereign runtime environment...$($S.R)"

# 1. Telemetry and Sandbox Setup
$ND = New-Item -ItemType Directory -Path (Join-Path $HOME ".nyx") -Force -ErrorAction SilentlyContinue
try { $R = [Math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 2) } catch { $R = 4.0 }

# 2. Dynamic Hardware Mapping Array
$P = ($R -lt 1.0) ? "SOVEREIGN_CLOUD" : (($R -lt 4.0) ? "LOCAL_COMPRESSED" : "LOCAL_ACCELERATED")
$M = ($P -eq "SOVEREIGN_CLOUD") ? "none" : (($P -eq "LOCAL_COMPRESSED") ? "qwen2.5-coder:1.5b" : "qwen2.5-coder:7b")

if ($P -ne "SOVEREIGN_CLOUD" -and (Get-Command "ollama" -ErrorAction SilentlyContinue)) {
    if (-not (Get-Process "ollama" -ErrorAction SilentlyContinue)) { Start-Process "ollama" "serve" -WindowStyle Hidden }
    Start-Process "ollama" "pull $M" -NoNewWindow -Wait
} else { $P = "SOVEREIGN_CLOUD"; $M = "none" }

# Save system config configuration
@{Profile=$P; Model=$M; Update=(Get-Date -F "yyyy-MM-dd")} | ConvertTo-Json | Out-File (Join-Path $HOME ".nyx/config.json") -Encoding utf8

# 3. Micro Shell Profile Injection Loop
$PR = $PROFILE.CurrentUserAllHosts; if (-not (Test-Path $PR)) { $null = New-Item -ItemType File -Path $PR -Force }
$H = @"
# ─── NYX RUNTIME HOOK ───
if (Test-Path (Join-Path `$HOME ".nyx")) {
    function global:nyx {
        `$E = [char]27; `$S = @{V="`$E[38;2;135;95;255m";C="`$E[38;2;0;255;255m";R="`$E[0m"}
        `$C = Get-Content (Join-Path `$HOME ".nyx/config.json") | ConvertFrom-Json
        Write-Host "`n`$(`$S.V)   🐈 NYX ENGINE (`$(`$C.Profile)):`$(`$S.C) Active via `$(`$C.Model)...`$(`$S.R)"
        `$T = [PowerShell]::Create(); `$Pool = [runspaces.runspacefactory]::CreateRunspacePool(1,2); [void]`$Pool.Open(); `$T.RunspacePool = `$Pool
    }
}
"@

if ((Get-Content $PR -Raw -EA SilentlyContinue) -notlike "*NYX RUNTIME HOOK*") { Add-Content $PR "`n$H" }
Write-Host "$($S.J)✔ Optimization deployed successfully. Restart terminal and enter 'nyx'.$($S.R)`n"
