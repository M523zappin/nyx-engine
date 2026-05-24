import os
import torch
import asyncio
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Static

# AUTHENTICATION
os.environ["HF_TOKEN"] = "Hf_YPrDaunNXWwVMOZcTGRFsYvttwsaDYXusG"

class NYX(App):
    """
    NYX // SOVEREIGN_KERNEL // v21.0 // PERSISTENT_STATE
    - Architecture: Preloaded Identity-Aware Inference Engine.
    """
    
    CSS = """
    Screen { background: #000; }
    #header { height: 1; background: #1a1a1a; color: #888; padding: 0 1; text-align: right; }
    Log { width: 100%; height: 1fr; background: #000; color: #ddd; padding: 1; }
    Input { width: 100%; height: 3; background: #000; color: #fff; border-top: solid #333; }
    """

    def compose(self) -> ComposeResult:
        yield Static("NYX // IDENTITY_LOCKED // STATE: PRELOADED", id="header")
        yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def on_mount(self) -> None:
        self.query_one("#input", Input).focus()
        self.log_msg(">> Initializing NYX Persona...")
        
        # Preloading the identity-model
        try:
            # We use the Phi-3-mini as the core identity model
            self.pipe = pipeline("text-generation", model="microsoft/Phi-3-mini-4k-instruct", device="cpu")
            self.log_msg(">> NYX Identity Preloaded. Sovereign State Active.")
        except Exception as e:
            self.log_msg(f">> FAULT: {str(e)}")

    def log_msg(self, msg):
        self.query_one(Log).write(msg)

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value.strip()
        event.input.value = ""
        
        if self.pipe:
            self.log_msg(f"👤 {cmd}")
            loop = asyncio.get_event_loop()
            res = await loop.run_in_executor(None, lambda: self.pipe(cmd, max_new_tokens=150))
            self.log_msg(f"✨ NYX: {res[0]['generated_text'].replace(cmd, '').strip()}")
        else:
            self.log_msg(">> ALERT: Engine initialization failed.")

if __name__ == "__main__":
    NYX().run()
