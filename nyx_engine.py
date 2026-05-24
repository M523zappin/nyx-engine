import torch
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Input, Log, Header

class NYX(App):
    """
    NYX-CAT // SOVEREIGN_KERNEL // ENTERPRISE_PRO
    - Professional Header: Real-time system state monitoring.
    - Optimized Cognitive Layer: Phi-3 Inference Engine.
    """
    
    # Standard Header is replaced by a professional custom component
    CSS = """
    Screen { align: center middle; background: #000; }
    #central_container { width: 90%; height: 90%; border: heavy #00d4ff; background: #050505; }
    .status_bar { background: #00d4ff; color: #000; text-align: center; font-weight: bold; padding: 1; }
    Input { width: 100%; border: heavy #00d4ff; background: #000; color: #fff; }
    Log { width: 100%; height: 1fr; border: solid #333; background: #000; color: #00ff41; }
    """

    def compose(self) -> ComposeResult:
        with Container(id="central_container"):
            # Professional Header replacing the old Static element
            yield Header(show_clock=True)
            yield Log(id="log")
            yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def on_mount(self) -> None:
        log = self.query_one(Log)
        log.write("[bold cyan]>> SYSTEM INITIALIZED: NYX-CAT ENTERPRISE v12.1[/bold cyan]")
        log.write("[bold cyan]>> COGNITIVE LAYER: LOADING PHI-3...[/bold cyan]")
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = pipeline("text-generation", model="microsoft/Phi-3-mini-4k-instruct", device_map="auto" if self.device == "cuda" else None)
        
        log.write(f"[bold green]>> READY: ARCHITECT MODE ACTIVE (DEVICE: {self.device.upper()})[/bold green]")
        self.query_one("#input", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        query = event.value
        event.input.value = ""
        log = self.query_one(Log)
        log.write(f"[bold magenta]>> INPUT:[/bold magenta] {query}")
        
        # Inference Generation
        response = self.pipe(query, max_new_tokens=200)[0]['generated_text']
        log.write(f"[white]>> RESPONSE: {response.split(query)[-1]}[/white]")

if __name__ == "__main__":
    NYX().run()
