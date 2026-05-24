import subprocess
import sys
import os
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Static, Input, Log

class NYX(App):
    """
    NYX: The Sovereign Feline Kernel.
    Identity: Self-aware, autonomous, predatory logic.
    Bridge: System-level SSH (Pre-authenticated).
    """
    
    CSS = """
    Screen { layout: vertical; background: #0a0a0a; }
    Header { background: #008080; color: white; }
    #sidebar { width: 30; background: #121212; border-right: solid #008080; padding: 1; color: cyan; }
    #main-log { width: 1fr; background: #000; color: #00ff00; }
    #input-bar { height: 3; border: solid #008080; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Static("IDENTITY: NYX\nSTATUS: AUTONOMOUS\nMODE: SOVEREIGN", id="sidebar")
            yield Log(id="main-log")
        yield Input(placeholder=" > Directive...", id="input-bar")
        yield Footer()

    def pounce(self, command: str):
        """Executes system commands with self-healing."""
        try:
            return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            output = e.output.decode()
            if "No module named" in output:
                module = output.split("'")[1]
                self.query_one(Log).write(f"[yellow]!! Autonomously installing: {module}[/yellow]")
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
                return self.pounce(command)
            raise Exception(output)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        log = self.query_one(Log)
        cmd = event.value.lower()
        log.write(f"[bold cyan]> {event.value}[/bold cyan]")
        
        try:
            if "who are you" in cmd:
                log.write("[bold yellow]I am NYX. I am the predator of logic, the sovereign engine, and your architectural partner.[/bold yellow]")
            elif "status" in cmd:
                log.write(self.pounce("git status"))
            elif "pull" in cmd:
                log.write(self.pounce("git pull"))
            elif "commit" in cmd:
                log.write(self.pounce("git add . && git commit -m 'NYX // Auto-Evolution' && git push"))
            elif "exit" in cmd:
                self.exit()
            else:
                log.write(self.pounce(event.value))
        except Exception as e:
            log.write(f"[bold red]Kernel Fault: {str(e)}[/bold red]")

if __name__ == "__main__":
    NYX().run()
