Nyx is a native, persistent terminal kernel engineered for zero-latency execution. By moving from interpreted scripting to a compiled Daemon-Client architecture, Nyx provides a dedicated, state-aware interface that operates independently of local shell profile bloat.
🛠️ Architectural Foundation
• Sovereign Execution Pool (SEP): The persistent nyx-daemon.exe core that maintains memory, manages the Skill Registry, and processes requests without overhead.
• IPC-Driven Interface: The nyx.exe client utilizes Named Pipes to communicate directly with the daemon, bypassing standard shell initialization lag.
• Zero-Conflict Logic: Nyx avoids shell profile hooks, ensuring total environment isolation and immunity to shell-based interference.
🚀 Build & Deployment
1.	Initialize: Ensure your workspace is located at %USERPROFILE%\.nyx.
2.	Compile: Generate the binaries using the C# compiler (csc):
• csc /target:exe /out:"%USERPROFILE%\.nyx\nyx-daemon.exe" "%USERPROFILE%\.nyx\NyxKernel.cs"
• csc /target:exe /out:"%USERPROFILE%\.nyx\nyx.exe" "%USERPROFILE%\.nyx\nyx.cs"
3.	Bootstrap: Launch nyx-daemon.exe to initiate the Sovereign Execution Pool.
4.	Execute: Run nyx <command> from any terminal window to interface with the kernel.
🧠 Evolution Path
Nyx is an autonomous system. Every agent connection is indexed into the local registry.db. This allows for Skill Grafting, where the kernel learns, categorizes, and executes complex workflows, effectively evolving into a self-contained AI operating system.
Why this is the correct text:
