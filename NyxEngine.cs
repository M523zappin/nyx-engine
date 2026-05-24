import os
import time
import sys
import threading
import hashlib

# ANSI Colors for Visual Identity
COLORS = {"R": "\033[91m", "G": "\033[92m", "Y": "\033[93m", "B": "\033[94m", "C": "\033[96m", "RESET": "\033[0m"}

class SovereignBrain:
    def __init__(self, storage=".nyx_memory.bin"):
        self.storage = storage

    def graft(self, prompt, response):
        with open(self.storage, "a") as f:
            f.write(f"{hashlib.md5(prompt.encode()).hexdigest()}|{prompt}|{response}\n")

    def recall(self, prompt):
        search_hash = hashlib.md5(prompt.encode()).hexdigest()
        if not os.path.exists(self.storage): return None
        with open(self.storage, "r") as f:
            for line in f:
                if line.startswith(search_hash): return line.split("|")[2]
        return None

# Global State
brain = SovereignBrain()
last_response = "System Initialized. Awaiting Directive."
is_running = True

def input_bus():
    global last_response
    while is_running:
        # Move cursor to bottom for chat
        sys.stdout.write(f"\033[15;1H{COLORS['C']} > {COLORS['RESET']}")
        sys.stdout.flush()
        cmd = sys.stdin.readline().strip()
        if cmd.lower() in ["exit", "quit"]: break
        
        recalled = brain.recall(cmd)
        if recalled:
            last_response = f"Recalled: {recalled[:35]}..."
        else:
            last_response = "Synthesizing tactical response..."
            brain.graft(cmd, "Optimized execution sequence.")

def render_ui():
    sys.stdout.write("\033[2J\033[?25l") # Clear and Hide Cursor
    while is_running:
        sys.stdout.write("\033[H") # Snap to top
        pulse = int(time.time() % 2)
        c = COLORS['G'] if pulse == 0 else COLORS['C']
        
        ui = [
            f"{c}╔══════════════════════════════════════════════════════╗{COLORS['RESET']}",
            f"{c}║           NYX-CAT SOVEREIGN INTELLIGENCE             ║{COLORS['RESET']}",
            f"{c}╠══════════════════════════════════════════════════════╣{COLORS['RESET']}",
            f"{c}║{COLORS['RESET']} STATUS: {COLORS['Y']}AUTONOMOUS{COLORS['RESET']} ACTIVE                        {c}║{COLORS['RESET']}",
            f"{c}║{COLORS['RESET']} MEMORY: {brain.storage}                      {c}║{COLORS['RESET']}",
            f"{c}║{COLORS['RESET']} LAST: {last_response[:40]:<39} {c}║{COLORS['RESET']}",
            f"{c}╚══════════════════════════════════════════════════════╝{COLORS['RESET']}",
            f"\n{COLORS['Y']}CHAT BOX:{COLORS['RESET']}"
        ]
        for line in ui: sys.stdout.write(line + "\033[K\n")
        sys.stdout.flush()
        time.sleep(0.5)

# Launch
threading.Thread(target=render_ui, daemon=True).start()
input_bus()
sys.stdout.write("\033[?25h") # Restore Cursor
