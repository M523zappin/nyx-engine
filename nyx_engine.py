import torch
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Log, Static

class NYX(App):
    """
    NYX-CAT // SOVEREIGN_KERNEL // v13.0 // QUANTIZED
    - Architecture: 4-bit Quantized Phi-3 Inference Engine.
    - Stability: Zero-conflict widget layout.
    """
    
    CSS = """
    Screen { background: #000; }
    #header_bar { background: #00d4ff; color: #000; text-align: center; height: 3; font-weight: bold; }
    Log { width: 100%; height: 1fr; border: solid #333; background: #000; color: #00ff41; }
    Input { width: 100%; height: 3; border: heavy #00d4ff; background: #000; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        yield Static("NYX-CAT // SOVEREIGN ARCHITECT // ENTERPRISE v13.0", id="header_bar")
        yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def on_mount(self) -> None:
        log = self.query_one(Log)
        log.write(">> INITIALIZING COGNITIVE ENGINE (4-BIT)...")
        
        try:
            # Using 4-bit quantization for maximum RAM efficiency
            self.pipe = pipeline(
                "text-generation", 
                model="microsoft/Phi-3-mini-4k-instruct",
                model_kwargs={"load_in_4bit": True, "device_map": "auto"}
            )
            log.write(">> COGNITIVE ENGINE ONLINE.")
        except Exception as e:
            log.write(f">> FATAL ERROR: {str(e)}")
            
        self.query_one("#input", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        query = event.value
        event.input.value = ""
        log = self.query_one(Log)
        log.write(f">> INPUT: {query}")
        
        # Inference Generation
        response = self.pipe(query, max_new_tokens=150)[0]['generated_text']
        clean_response = response.replace(query, "")
        log.write(f">> NYX: {clean_response.strip()}")

if __name__ == "__main__":
    NYX().run()
