"""
NYX // MAIN TERMINAL INTERFACE
"""
import sys
import sentinel
import evolution

class NyxNode:
    def __init__(self):
        self.brain = evolution.SovereignBrain()

    def run(self):
        # Scan core code for unauthorized modifications before booting
        if not sentinel.check_code("NyxEngine.py"):
            print("CRITICAL: Code integrity failure. Boot halted.")
            sys.exit(1)
        
        # Enter full screen terminal buffer
        sys.stdout.write("\033[?1049h\033[2J")
        try:
            while True:
                sys.stdout.write(f"\033[H\033[1;36mNYX // SOVEREIGN NODE // STATUS: SECURE\033[0m\n\033[2;1HCHAT >> ")
                sys.stdout.flush()
                
                user_input = sys.stdin.readline().strip()
                if user_input.lower() == "exit": 
                    break
                
                if not user_input:
                    continue

                sys.stdout.write("\n[THINKING...]\n")
                
                # Internal reasoning generation
                response = self.brain.infer(user_input)
                
                # Telemetry logging and self-training checks
                evolution.EvolutionaryEngine.log_interaction(user_input, response)
                evolution.AutonomyManager.check_evolution_readiness()
                
                # Reload updated weight states if an evolution occurred
                self.brain.load_weights()
                
                sys.stdout.write(f"\nNYX: {response}\n\n")
                sys.stdout.write("Press ENTER to continue...")
                sys.stdin.readline()
                sys.stdout.write("\033[2J") # Clear screen for next turn
        finally:
            # Cleanly restore standard terminal view on exit
            sys.stdout.write("\033[?1049l")

if __name__ == "__main__":
    NyxNode().run()
