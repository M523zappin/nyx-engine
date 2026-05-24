import os
import time
import sys
import threading

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

user_input = ""
last_response = "Nyx is ready to hunt. Type a command..."

def input_listener():
    global user_input, last_response
    while True:
        # Move cursor to bottom for typing
        sys.stdout.write(f"\033[15;1H{CYAN} > {RESET}")
        sys.stdout.flush()
        cmd = sys.stdin.readline().strip()
        if cmd:
            last_response = f"Nyx processed: '{cmd}'" # Logic hook for your AI backend
            user_input = ""

def draw_dashboard():
    sys.stdout.write("\033[2J\033[?25l")
    while True:
        sys.stdout.write("\033[H")
        pulse = int(time.time() % 2)
        color = GREEN if pulse == 0 else CYAN
        
        output = [
            f"{color}╔══════════════════════════════════════════════════════╗{RESET}",
            f"{color}║           NYX SOVEREIGN INTELLIGENCE v1.0            ║{RESET}",
            f"{color}╠══════════════════════════════════════════════════════╣{RESET}",
            f"{color}║{RESET} LAST: {last_response[:40]:<39} {color}║{RESET}",
            f"{color}╚══════════════════════════════════════════════════════╝{RESET}",
            f"\n{YELLOW}CHAT BOX:{RESET}"
        ]
        
        for line in output:
            sys.stdout.write(line + "\033[K\n")
        sys.stdout.flush()
        time.sleep(0.1)

# Start Threads
threading.Thread(target=input_listener, daemon=True).start()
draw_dashboard()
