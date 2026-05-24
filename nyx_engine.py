import os
import torch
import asyncio
from concurrent.futures import ThreadPoolExecutor
from transformers import pipeline
from textual.app import App, ComposeResult
from textual.widgets import Input, Log, Static
from textual.worker import Worker

# AUTHENTICATION
os.environ["HF_TOKEN"] = "Hf_YPrDaunNXWwVMOZcTGRFsYvttwsaDYXusG"

class NYX(App):
    """
    NYX-CAT // SOVEREIGN ARCHITECT // v18.0 // STABLE
    - Pattern: Worker-Thread Inference (Non-blocking UI)
    - Architecture: Event-driven command handling
    """
    CSS = """
    Screen { background: #000; }
    #header { height: 3; background: #00d4ff; color: #000; text-align: center; text-style: bold; content-align: center middle; }
    Log { width: 100%; height: 1fr; border: solid #333; background: #000; color: #00ff41; padding: 1; }
    Input { width: 100%; height: 3; border: heavy #00d4ff; background: #111; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        yield Static("NYX-CAT // SOVEREIGN ARCHITECT // v18.0", id="header")
        yield Log(id="log")
        yield Input(placeholder="🐾 Awaiting Directive...", id="input")

    def on_mount(self) -> None:
        self.pipe = None
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.query_one("#input", Input).focus()
        self.query_one(Log).write(">> NYX-CAT v18.0 // WORKER-THREAD ACTIVE.")

    async def run_inference(self, prompt: str):
        """Runs in background to prevent UI lag."""
        try:
            loop = asyncio.get_event_loop()
            res = await loop.run_in_executor(self.executor, lambda: self.pipe(prompt, max_new_tokens=100))
            return res[0]['generated_text'].replace(prompt, "").strip()
        except Exception as e:
            return f"FAULT: {str(e)}"

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value
        event.input.value = ""
        log = self.query_one(Log)
        
        if cmd.lower().startswith("load "):
            model_id = cmd.split(" ")[1]
            log.write(f">> EVOLVING BRAIN: {model_id}...")
            # Still blocking for the model load itself, but logic is clean
            self.pipe = pipeline("text-generation", model=model_id, device="cpu")
            log.write(">> EVOLUTION SUCCESS.")
        elif self.pipe:
            log.write(f">> INPUT: {cmd}")
            # Non-blocking worker execution
            self.run_worker(self.run_inference(cmd))
        else:
            log.write(">> ALERT: Engine empty. Execute 'LOAD <model_id>' first.")

    def run_worker(self, coroutine):
        # Textual worker integration
        self.run_worker = self.run_worker_func(coroutine)
    
    async def run_worker_func(self, coroutine):
        res = await coroutine
        self.query_one(Log).write(f">> NYX: {res}")

if __name__ == "__main__":
    NYX().run()
