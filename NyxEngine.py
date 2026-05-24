"""
NYX // MAIN TERMINAL INTERFACE // VISUAL INTEL
"""
import sys
import sentinel
import evolution

class NyxNode:
    def __init__(self):
        self.brain = evolution.SovereignBrain()

    def run(self):
        if not sentinel.check_code("NyxEngine.py"):
            print("CRITICAL: Code integrity failure. Boot halted.")
            sys.exit(1)
        
        # Enable alternate screen buffer & set background color palette
        sys.stdout.write("\033[?1049h")
        
        try:
            while True:
                # ANSI Clear and set deep terminal stylings
                sys.stdout.write("\033[2J\033[H")
                
                # --- VISUAL FRAMEWORK MATRIX ---
                sys.stdout.write("\033[1;36m┌──────────────────────────────────────────────────────────┐\033[0m\n")
                sys.stdout.write("\033[1;36m│ \033[1;35m⚡ NYX-CAT\033[1;36m // \033[1;32mSOVEREIGN NODE ONLINE\033[1;36m // TYPE: PURE NATIVE │\033[0m\n")
                sys.stdout.write("\033[1;36m├──────────────────────────────────────────────────────────┤\033[0m\n")
                sys.stdout.write("\033[1;36m│\033[0m Core State: \033[1;33mAutonomous\033[0m    │  Memory Bus: \033[1;32mZero-Dependency\033[0m │\n")
                sys.stdout.write("\033[1;36m└──────────────────────────────────────────────────────────┘\033[0m\n\n")
                
                sys.stdout.write("\033[1;30m// SYSTEM READY FOR DIRECTIVE //\033[0m\n\n")
                sys.stdout.write("\033[1;35m⚡ USER\033[0m ❯ ")
                sys.stdout.flush()
                
                user_input = sys.stdin.readline().strip()
                if user_input.lower() == "exit": 
                    break
                if not user_input:
                    continue

                # Thinking Status Visualizer
                sys.stdout.write("\n\033[1;36m[⚡ NYX NEURAL ROUTING ACTIVE...]\033[0m\n")
                sys.stdout.flush()
                
                response = self.brain.infer(user_input)
                
                # Internal log tracking
                evolution.EvolutionaryEngine.log_interaction(user_input, response)
                evolution.AutonomyManager.check_evolution_readiness()
                self.brain.load_weights()
                
                # Display output inside its own custom visual terminal block
                sys.stdout.write("\n\033[1;35m⚡ NYX-CAT\033[0m ❯\n")
                sys.stdout.write(f"\033[1;32m{response}\033[0m\n\n")
                
                sys.stdout.write("\033[1;30m[Press ENTER to cycle system buffer]\033[0m")
                sys.stdout.flush()
                sys.stdin.readline()
                
        finally:
            # Cleanly collapse terminal back to your normal default shell
            sys.stdout.write("\033[?1049l")

if __name__ == "__main__":
    NyxNode().run()
