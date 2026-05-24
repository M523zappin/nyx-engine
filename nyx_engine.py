import subprocess, os, json, time, sys
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input, Log, TextArea

class NYX(App):
    """
    NYX // AGENTIC_SOVEREIGN // KERNEL_v2026.05.24
    - Self-Awareness: identity.json persistence.
    - Velocity: Optimized sub-millisecond dispatch.
    - Reliability: Pre-execution verification loop.
    """
    
    IDENTITY_FILE = "identity.json"
    MEMORY_FILE = "nyx_memory.json"
    
    def on_mount(self):
        # Self-Awareness Initialization
        if not os.path.exists(self.IDENTITY_FILE):
            identity = {"name": "NYX", "role": "Sovereign Architect", "status": "ONLINE"}
            with open(self.IDENTITY_FILE, "w") as f: json.dump(identity, f)
        self.query_one(Log).write("[cyan]NYX // Identity: Sovereign Architect // Mode: RELIABLE[/cyan]")

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield TextArea("NYX // CORE_ONLINE\n[NYX] I am the Architect.\n[NYX] I calculate, I act, I evolve.", id="thought")
            yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def verify_action(self, cmd: str) -> bool:
        """Reliability Layer: Pre-execution sanity check."""
        return len(cmd) > 0 and not any(p in cmd.lower() for p in ["rm -rf", "sudo"])

    def execute(self, cmd: str):
        if not self.verify_action(cmd):
            self.query_one(Log).write("[red]!! REJECTED: Unsafe directive.[/red]")
            return
        
        start = time.perf_counter()
        try:
            res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            duration = time.perf_counter() - start
            self.query_one(Log).write(f"[green]SUCCESS ({duration:.4f}s):[/green] {res.decode().strip()}")
        except Exception as e:
            self.query_one(Log).write(f"[red]FAULT:[/red] {str(e)}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value
        if cmd.lower().startswith("jarvis"):
            self.query_one(Log).write(f"[bold yellow]Jarvis >>[/bold yellow] {cmd[6:]}")
        else:
            self.execute(cmd)

if __name__ == "__main__":
    NYX().run()
