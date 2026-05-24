# Nyx: Autonomous Sovereign Intelligence (ASI)

Nyx is a self-evolving, persistent R&D kernel engineered for zero-latency autonomous execution. By leveraging an IPC-driven architecture and a persistent Sovereign Execution Pool (SEP), Nyx operates independently of legacy shell constraints to function as your personal AI operating system.

## 🧠 Architectural Foundation
* **Sovereign Execution Pool (SEP):** A persistent background daemon (`nyx-daemon.exe`) that manages logic, memory, and autonomic observation.
* **Ghost-Buffer TUI:** A high-performance terminal interface that utilizes the Alternate Screen Buffer to create a lag-free, application-grade workspace without shell bloat.
* **Autonomic Observation Loop:** Nyx monitors `~\.nyx\inbox\` for task manifests, synthesizing logic and grafting skills into the `registry.db` autonomously.
* **Relational Intelligence:** A robust SQLite memory layer with auto-incrementing audit trails and thread-safe concurrency.

## 🚀 Deployment
1. **Initialize Workspace:** Create `%USERPROFILE%\.nyx\inbox` and `\outbox`.
2. **Compile:**
   ```bash
   csc /target:exe /out:"%USERPROFILE%\.nyx\nyx-daemon.exe" NyxKernel.cs RegistryManager.cs /r:System.Data.SQLite.dll
   csc /target:exe /out:"%USERPROFILE%\.nyx\nyx.exe" nyx.cs
