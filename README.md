# Nyx: Sovereign Terminal Kernel

Nyx is a native, persistent terminal kernel engineered for zero-latency execution. By moving from interpreted scripting to a compiled Daemon-Client architecture, Nyx provides a dedicated, state-aware interface that operates independently of local shell profile bloat.

### 🛠️ Architectural Foundation
* **Sovereign Execution Pool (SEP):** The persistent `nyx-daemon.exe` core maintains memory, manages the Skill Registry, and processes requests without overhead.
* **IPC-Driven Interface:** The `nyx.exe` client utilizes Named Pipes to communicate directly with the daemon, bypassing standard shell initialization lag.
* **Zero-Conflict Logic:** Nyx avoids shell profile hooks, ensuring total environment isolation.

### 🚀 Build & Deployment
1. **Initialize:** Ensure your workspace is located at `%USERPROFILE%\.nyx`.
2. **Compile:** Generate binaries using the C# compiler (`csc`):
   - `csc /target:exe /out:"%USERPROFILE%\.nyx\nyx-daemon.exe" NyxKernel.cs RegistryManager.cs /r:System.Data.SQLite.dll`
   - `csc /target:exe /out:"%USERPROFILE%\.nyx\nyx.exe" nyx.cs`
3. **Bootstrap:** Launch `nyx-daemon.exe` to initiate the Sovereign Execution Pool.
4. **Execute:** Run `nyx <command>` from any terminal window.

### 🧠 Evolution Path
Nyx is an autonomous system. Every agent connection is indexed into the local `registry.db` for "Skill Grafting," enabling the kernel to learn, categorize, and execute complex workflows as your personal AI operating system.
