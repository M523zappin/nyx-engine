import os
import torch
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Static

# AUTHENTICATION
os.environ["HF_TOKEN"] = "Hf_YPrDaunNXWwVMOZcTGRFsYvttwsaDYXusG"

class NYX_UI(App):
    """
    NYX-CAT // SOVEREIGN_UI // v16.0
    - The Display Layer: Flicker-free, focus-hardened TUI.
    """
    
    CSS = """
    Screen { background: #000; }
    #header { background: #00d4ff; color: #000; text-align: center; height: 3; text-style: bold; content-align: center middle; }
    Log { width: 100%; height: 1fr; border: solid #333; background: #000; color: #00ff41; }
    Input { width: 100%; height: 3; border: heavy #00d4ff; background: #000; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        yield Static("NYX-CAT // SOVEREIGN ARCHITECT // V16.0", id="header")
        yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def on_mount(self) -> None:
        self.query_one("#input", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value
        event.input.value = ""
        # Pass logic to the kernel logic controller
        self.post_message(LogicAction(cmd))

class LogicAction(Message):
    def __init__(self, command):
        self.command = command
        super().__init__()

# Logic Controller
class LogicController:
    def __init__(self):
        self.pipe = None
    
    def process(self, cmd):
        if cmd.lower().startswith("load "):
            model_id = cmd.split(" ")[1]
            self.pipe = pipeline("text-generation", model=model_id, device="cpu")
            return f"EVOLVED TO: {model_id}"
        elif self.pipe:
            res = self.pipe(cmd, max_new_tokens=100)[0]['generated_text']
            return f"NYX: {res.replace(cmd, '').strip()}"
        return "ALERT: Engine offline. Type 'LOAD modelname' first."

if __name__ == "__main__":
    app = NYX_UI()
    app.run()

