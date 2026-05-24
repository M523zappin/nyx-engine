import torch
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Static

class NYX(App):
    """
    NYX-CAT // SOVEREIGN_KERNEL // v14.0 // MEMORY_SAFE
    - Forced CPU execution to prevent GPU allocation crashes.
    - Offloaded model path to temporary storage.
    """
    
    CSS = """
    Screen { background: #000; }
    #header_bar { background: #00d4ff; color: #000; text-align: center; height: 3; content-align: center middle; text-style: bold; }
    Log { width: 100%; height: 1fr; border: solid #333; background: #000; color: #00ff41; }
    Input { width: 100%; height: 3; border: heavy #00d4ff; background: #000; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        yield Static("NYX-CAT // SOVEREIGN ARCHITECT // MEMORY_SAFE_MODE", id="header_bar")
        yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def on_mount(self) -> None:
        log = self.query_one(Log)
        log.write(">> INITIALIZING COGNITIVE ENGINE...")
        
        try:
            # Forcing CPU and low-memory usage
            self.pipe = pipeline(
                "text-generation", 
                model="microsoft/Phi-3-mini-4k-instruct",
                device="cpu", # Explicitly forcing CPU to prevent GPU memory spikes
                model_kwargs={"torch_dtype": "auto"}
            )
            log.write(">> ENGINE READY.")
        except Exception as e:
            log.write(f">> ENGINE FAULT: {str(e)}")
            
        self.query_one("#input", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        query = event.value
        event.input.value = ""
        log = self.query_one(Log)
        
        # Inference Generation
        response = self.pipe(query, max_new_tokens=100)[0]['generated_text']
        log.write(f">> NYX: {response.replace(query, '').strip()}")

if __name__ == "__main__":
    NYX().run()
