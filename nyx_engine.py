import os, torch
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Static

# AUTHENTICATION: Injecting your Sovereign Token
os.environ["HF_TOKEN"] = "Hf_YPrDaunNXWwVMOZcTGRFsYvttwsaDYXusG"

class NYX(App):
    """
    NYX-CAT // SWARM_MIND // v15.0
    - Model Agnostic: Swaps models via command.
    - Memory-Mapped: Prevents RAM overflow.
    """
    
    CSS = """
    Screen { background: #000; }
    #header_bar { background: #555; color: #fff; text-align: center; height: 3; content-align: center middle; }
    Log { width: 100%; height: 1fr; background: #000; color: #00ff41; }
    Input { width: 100%; height: 3; border: heavy #555; background: #111; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        yield Static("NYX-CAT // SWARM_MIND // READY FOR DIRECTIVE", id="header_bar")
        yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect (e.g., 'LOAD modelname')...", id="input")

    def on_mount(self) -> None:
        self.query_one(Log).write(">> SWARM_MIND ONLINE. AUTHENTICATED.")
        self.query_one("#input", Input).focus()

    def load_model(self, model_id: str):
        log = self.query_one(Log)
        log.write(f">> EVOLVING TO: {model_id}...")
        try:
            self.pipe = pipeline("text-generation", model=model_id, device="cpu")
            log.write(">> EVOLUTION COMPLETE.")
        except Exception as e:
            log.write(f">> EVOLUTION FAILED: {str(e)}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        query = event.value
        event.input.value = ""
        
        if query.lower().startswith("load "):
            self.load_model(query.split(" ")[1])
        elif hasattr(self, 'pipe'):
            res = self.pipe(query, max_new_tokens=100)[0]['generated_text']
            self.query_one(Log).write(f">> NYX: {res.replace(query, '').strip()}")
        else:
            self.query_one(Log).write(">> ALERT: Load a model first (e.g., LOAD microsoft/Phi-3-mini-4k-instruct)")

if __name__ == "__main__":
    NYX().run()
