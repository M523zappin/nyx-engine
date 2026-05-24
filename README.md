# 🐈 Nyx Engine: Sovereign Build Specification

Nyx is a native terminal kernel. It avoids shell profile hooks, opting for direct binary mapping to ensure the interface never conflicts with your local shell settings.

## 🛠️ Build Structure
- **Core Engine:** `engine.ps1` maintains an isolated render-loop in the terminal's alternate screen buffer.
- **Binary Mapping:** `nyx.bat` provides direct access to the Sovereign Execution Pool.
- **Latency-Free UI:** High-frequency rendering via the `1049` buffer sequence.

## 🚀 Execution
1. Place `engine.ps1` in your repo.
2. Run `install.ps1`.
3. Call `nyx` from any terminal window.
