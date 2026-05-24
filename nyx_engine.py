import subprocess, os, json, time
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input, Log, TextArea

class NYX(App):
    """
    NYX // AGENTIC_SOVEREIGN // FOCUS_HARDENED
    - Forced-Focus Logic: Input claims focus on mount.
    - Minimalist Layout: Removes layout ambiguity.
    """
    
    CSS = """
    Screen { background: #000; layout: vertical; }
    #thought { height: 10; border: heavy #00d4ff; background: #050505; color: #00d4ff; }
    #log { height: 1fr; border: heavy #00d4ff; background: #000; color: #00ff41; }
    #input { height: 3; border: heavy #00d4ff; background: #000; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        yield TextArea("NYX // CORE_ONLINE\n[NYX] Focus: Claimed.\n[NYX] Directives active.", id="thought")
        yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def on_mount(self) -> None:
        """Force focus to the input widget immediately on start."""
        self.query_one("#input", Input).focus()

    def execute_directive(self, cmd: str):
        log = self.query_one(Log)
        # Bypassing complex shell logic for maximum reliability
        try:
            # We run the command and capture the output safely
            res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            log.write(f"[green]SUCCESS:[/green] {res.decode().strip()}")
        except Exception as e:
            log.write(f"[red]FAULT:[/red] {str(e)}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value
        # Clear the input for the next command
        event.input.value = ""
        
        if cmd.lower().startswith("jarvis"):
            self.query_one(Log).write(f"[bold yellow]Jarvis >>[/bold yellow] {cmd[6:]}")
        else:
            self.execute_directive(cmd)

if __name__ == "__main__":
    NYX().run()
