"""
NYX // MAIN TERMINAL INTERFACE
"""
import sys
import sentinel
import evolution

class NyxNode:
    def __init__(self):
        # This will now find the class correctly
        self.brain = evolution.SovereignBrain()

    def run(self):
        # Verify code integrity before full-screen initialization
        if not sentinel.check_code("NyxEngine.py"):
            print("CRITICAL: Code integrity failure. Boot halted.")
            sys.exit(1)
        
        # Trigger an alternate terminal buffer (clear look screen)
        sys.stdout.write("\033[?1049h\033[2J")
        try:
            while True:
                # Fresh screen draw
                sys.stdout.write("\033[H\033[1;36m==================================================\033[0m\n")
                sys.stdout.write("\033[1;36m       NYX // SOVEREIGN NODE // STATUS: SECURE    \033[0m\n")
                sys.stdout.write("\033[1;36m==================================================\033[0m\n\n")
                sys.stdout.write("CHAT >> ")
                sys.stdout.flush()
                
                user_input = sys.stdin.readline().strip()
                if user_input.lower() == "exit": 
                    break
                
                if not user_input:
                    sys.stdout.write("\033[2J")
                    continue

                sys.stdout.write("\n[THINKING...]\n")
                
                # Fetch reasoning array output
                response = self.brain.infer(user_input)
                
                # Log state metrics
                evolution.EvolutionaryEngine.log_interaction(user_input, response)
                evolution.AutonomyManager.check_evolution_readiness()
                
                # Dynamic weight hot-reload
                self.brain.load_weights()
                
                sys.stdout.write(f"\nNYX: \033[1;32m{response}\033[0m\n\n")
                sys.stdout.write("Press ENTER to clear screen and continue...")
                sys.stdout.flush()
                sys.stdin.readline()
                sys.stdout.write("\033[2J") # Clear screen frame
        finally:
            # Cleanly restore your regular terminal when closing out
            sys.stdout.write("\033[?1049l")

if __name__ == "__main__":
    NyxNode().run()
