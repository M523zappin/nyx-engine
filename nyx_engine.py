import subprocess, os, json
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input, Log, TextArea

class NYX(App):
    """
    NYX // AGENTIC_KERNEL // PERSISTENT_MEMORY
    1. Agentic Logic: System/Build operations.
    2. Conversational Bridge: Intellectual exchange.
    3. Persistent Memory: JSON-based state retention.
    """
    
    MEMORY_FILE = "nyx_memory.json"

    def load_memory(self):
        if os.path.exists(self.MEMORY_FILE):
            with open(self.MEMORY_FILE, "r") as f:
                return json.load(f)
        return []

    def save_memory(self, entry):
        history = self.load_memory()
        history.append(entry)
        with open(self.MEMORY_FILE, "w") as f:
            json.dump(history, f)

    CSS = """
    Screen { background: #000; }
    #thought-pane { width: 40; border: heavy #00d4ff; background: #050505; color: #00d4ff; }
    #log-pane { width: 1fr; border: heavy #00d4ff; background: #000; color: #00ff41; }
    #input-bar { height: 3; border: heavy #00d4ff; background: #000; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield TextArea("NYX // PERSISTENT_MEMORY_ACTIVE", id="thought-pane")
            yield Log(id="log-pane")
        yield Input(placeholder=" 🐾 Chat or Direct...", id="input-bar")

    def on_mount(self) -> None:
        # Restore past context
        history = self.load_memory()
        log = self.query_one(Log)
        for entry in history[-5:]: # Show last 5 interactions
            log.write(f"[dim]History: {entry['input']}[/dim]")

    def process(self, text: str):
        log = self.query_one(Log)
        forbidden = ["rm -rf", "format", "sudo"]
        
        if any(f in text.lower() for f in forbidden):
            log.write("[bold red]SECURITY ALERT: Destructive intent blocked.[/bold red]")
            return

        # Save to Memory
        self.save_memory({"input": text})

        if text.lower().startswith("jarvis"):
            log.write(f"[bold yellow]Jarvis >>[/bold yellow] {text[6:]}")
        else:
            log.write(f"[bold cyan]NYX >>[/bold cyan] {text}")
            try:
                res = subprocess.check_output(text, shell=True, stderr=subprocess.STDOUT)
                log.write(f"[green]SUCCESS:[/green] {res.decode().strip()}")
            except Exception as e:
                log.write(f"[red]FAULT:[/red] {str(e)}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.process(event.value)

if __name__ == "__main__":
    NYX().run()
