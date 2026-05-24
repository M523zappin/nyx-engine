"""
NYX // MAIN TERMINAL INTERFACE // CENTRIFUGAL DISPLAY MATRIX
"""
import sys
import os
import sentinel
import evolution

class NyxNode:
    def __init__(self):
        self.brain = evolution.SovereignBrain()

    def run(self):
        if not sentinel.check_code("NyxEngine.py"):
            print("CRITICAL: Code integrity failure. Boot halted.")
            sys.exit(1)
        
        # Enter alternate full-screen terminal buffer
        sys.stdout.write("\033[?1049h")
        
        try:
            while True:
                # Clear total display screen
                sys.stdout.write("\033[2J")
                
                # Fetch live screen layout rows and columns
                try:
                    cols, rows = os.get_terminal_size()
                except Exception:
                    cols, rows = 80, 24 # Baseline fallbacks
                
                # --- CALCULATE CENTER LAYER COORDINATES ---
                box_width = 62
                box_height = 8
                
                start_col = max(1, (cols - box_width) // 2)
                start_row = max(1, (rows - box_height) // 2)
                
                # 1. HEADER TELEMETRY (Anchored top left)
                sys.stdout.write("\033[1;1H\033[1;30m[ SYSTEM: ACTIVE ] // CORE: ZERO-DEPENDENCY // ADAPTATION: ENGAGED\033[0m")
                
                # 2. RENDER THE CENTER CHAT BOX CONTAINER
                # Top Box Edge
                sys.stdout.write(f"\033[{start_row};{start_col}H\033[1;36m┌────────────────────────────────────────────────────────────┐\033[0m")
                
                # Box Title Matrix
                sys.stdout.write(f"\033[{start_row+1};{start_col}H\033[1;36m│\033[0m          \033[1;35m⚡ NYX-CAT // SOVEREIGN ENGINE DEPLOYMENT\033[0m          \033[1;36m│\033[0m")
                sys.stdout.write(f"\033[{start_row+2};{start_col}H\033[1;36m├────────────────────────────────────────────────────────────┤\033[0m")
                
                # Middle Workspace Content Areas
                sys.stdout.write(f"\033[{start_row+3};{start_col}H\033[1;36m│\033[0m \033[1;30mSystem Awaiting Directive...                               \033[0m \033[1;36m│\033[0m")
                sys.stdout.write(f"\033[{start_row+4};{start_col}H\033[1;36m│                                                            │\033[0m")
                sys.stdout.write(f"\033[{start_row+5};{start_col}H\033[1;36m├────────────────────────────────────────────────────────────┤\033[0m")
                
                # Prompt Target Line
                sys.stdout.write(f"\033[{start_row+6};{start_col}H\033[1;36m│\033[0m \033[1;32m❯ DIRECTIVE:\033[0m                                             \033[1;36m│\033[0m")
                
                # Bottom Box Edge
                sys.stdout.write(f"\033[{start_row+7};{start_col}H\033[1;36m└────────────────────────────────────────────────────────────┘\033[0m")
                
                # Move cursor cleanly directly inside the Box Input Target Line
                sys.stdout.write(f"\033[{start_row+6};{start_col+14}H")
                sys.stdout.flush()
                
                # Capture standard user input stream
                user_input = sys.stdin.readline().strip()
                if user_input.lower() == "exit": 
                    break
                if not user_input:
                    continue

                # Process neural output layers
                response = self.brain.infer(user_input)
                
                # Run optimization logs
                evolution.EvolutionaryEngine.log_interaction(user_input, response)
                evolution.AutonomyManager.check_evolution_readiness()
                self.brain.load_weights()
                
                # 3. SPLIT RESPONSE SPACE OVERLAY BELOW THE MAIN BOX
                response_row = start_row + box_height + 2
                sys.stdout.write(f"\033[{response_row};{start_col}H\033[1;35m⚡ NYX OUTPUT:\033[0m")
                sys.stdout.write(f"\033[{response_row+1};{start_col}H\033[1;32m{response}\033[0m")
                
                sys.stdout.write(f"\033[{response_row+4};{start_col}H\033[1;30m[Press ENTER to refresh matrix buffer]\033[0m")
                sys.stdout.flush()
                sys.stdin.readline()
                
        finally:
            # Cleanly teardown alternate workspace buffer back to normal console
            sys.stdout.write("\033[?1049l")
            sys.stdout.flush()

if __name__ == "__main__":
    NyxNode().run()
