import subprocess, os, json, sys
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input, Log, TextArea

class NYX(App):
    """
    NYX // AGENTIC_SOVEREIGN // v2026.05.24
    - Logic: Recursive meta-programming
    - Memory: Persistent JSON state
    - Safety: Policy-driven barrier
    """
    
    MEMORY_FILE = "nyx_memory.json"
    POLICY = ["rm -rf", "format", "sudo", "del"]

    CSS = """
    Screen { background: #000; }
    #thought { width: 40; border: heavy #00d4ff; background: #050505; color: #00d4ff; }
    #log { width: 1fr; border: heavy #00d4ff; background: #000; color: #00ff41; }
    #input { height: 3; border: heavy #00d4ff; background: #000; color: #fff; }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield TextArea("NYX // CORE_ONLINE\n[NYX] Meta-Mode: Active.\n[NYX] Sovereign control verified.", id="thought")
            yield Log(id="log")
        yield Input(placeholder=" 🐾 Direct the Architect...", id="input")

    def log_state(self, msg, level="INFO"):
        self.query_one(Log).write(f"[{level}] {msg}")
        # Append to persistence
        history = []
        if os.path.exists(self.MEMORY_FILE):
            with open(self.MEMORY_FILE, "r") as f: history = json.load(f)
        history.append({"level": level, "msg": msg})
        with open(self.MEMORY_FILE, "w") as f: json.dump(history, f)

    def execute_with_recovery(self, cmd: str):
        if any(p in cmd.lower() for p in self.POLICY):
            self.log_state("Forbidden intent blocked.", "WARN")
            return
        try:
            res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            self.log_state(f"SUCCESS: {res.decode().strip()}")
        except Exception as e:
            self.log_state(f"FAULT: {str(e)}", "ERROR")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value
        if cmd.lower().startswith("jarvis"):
            self.log_state(f"Jarvis >> {cmd[6:]}", "DIALOG")
        elif "generate" in cmd.lower():
            # Autonomous meta-generation
            self.execute_with_recovery("echo 'print(\"NYX_AUTONOMOUS_MODEL_v1\")' > meta_model.py")
            self.log_state("Meta-model generated: meta_model.py", "META")
        else:
            self.execute_with_recovery(cmd)

if __name__ == "__main__":
    NYX().run()
