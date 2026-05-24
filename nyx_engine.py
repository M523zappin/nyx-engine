import subprocess
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Input, Log, Static

class NYX(App):
    """
    NYX-CAT // SOVEREIGN_KERNEL // COGNITIVE_RELEASE
    - Logic Gate: Differentiates system tasks from cognitive inquiries.
    """
    
    CSS = """
    Screen { align: center middle; background: #000; }
    #central_container { width: 80%; height: 80%; border: heavy #00d4ff; background: #050505; }
    #prompt_area { padding: 1; text-align: center; color: #00d4ff; }
    Input { width: 100%; border: heavy #00d4ff; background: #000; color: #fff; }
    Log { width: 100%; height: 1fr; border: solid #333; background: #000; color: #00ff41; }
    """

    def compose(self) -> ComposeResult:
        with Container(id="central_container"):
            yield Static("[bold cyan]NYX-CAT // SOVEREIGN ARCHITECT // STATUS: ONLINE[/bold cyan]", id="prompt_area")
            yield Log(id="log")
            yield Input(placeholder=" 🐾 Direct the Architect or pose a query...", id="input")

    def on_mount(self) -> None:
        self.query_one("#input", Input).focus()

    def process_intelligence(self, query: str):
        """Cognitive processing for non-system queries."""
        # This simulates deep synthesis. In a production environment, 
        # this integrates with your local LLM vector store.
        log = self.query_one(Log)
        
        # Heuristic for intelligence: Does it look like a question?
        if "?" in query or any(w in query.lower() for w in ["explain", "why", "how", "what"]):
            log.write(f"[bold magenta]NYX-Cognition:[/bold magenta] Analyzing '{query}'...")
            log.write("[italic white]NYX-Synthesis:[/italic white] Your directive is clear. I am processing the logic layer to provide the optimal architectural path.")
        else:
            self.execute_system(query)

    def execute_system(self, cmd: str):
        log = self.query_one(Log)
        try:
            res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            log.write(f"[green]SUCCESS:[/green] {res.decode().strip()}")
        except Exception as e:
            log.write(f"[red]FAULT:[/red] {str(e)}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value
        event.input.value = ""
        log = self.query_one(Log)
        
        if cmd.lower().startswith("jarvis"):
            log.write(f"[yellow]Jarvis >>[/yellow] {cmd[6:]}")
        else:
            self.process_intelligence(cmd)

if __name__ == "__main__":
    NYX().run()
