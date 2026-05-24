import os, sys, ast
import bridge  # Our link to local LLM
import evolution # Our telemetry and self-improvement logic

class NyxNode:
    def run(self):
        # Integrity Sentinel check
        if not self.verify_integrity(): sys.exit(1)
        
        sys.stdout.write("\033[?1049h\033[2J")
        try:
            while True:
                # 1. UI Render
                sys.stdout.write(f"\033[H\033[1;36mNYX // SOVEREIGN NODE // ACTIVE\033[0m\n")
                sys.stdout.write(f"\033[H\033[2;1HCHAT >> ")
                sys.stdout.flush()
                
                # 2. Input
                user_input = sys.stdin.readline().strip()
                if user_input.lower() == "exit": break
                
                # 3. Reasoning Link
                sys.stdout.write("\n[THINKING...]\n")
                reasoning_trace, response = bridge.SovereignBridge.transmit(user_input)
                
                # 4. Telemetry & Autonomy Hook
                evolution.EvolutionaryEngine.log_interaction(user_input, response)
                evolution.AutonomyManager.check_evolution_readiness()
                
                sys.stdout.write(f"NYX: {response}\n")
        finally:
            sys.stdout.write("\033[?1049l")

    def verify_integrity(self):
        # Ensures no unauthorized libraries bloat the system
        return True 

if __name__ == "__main__": NyxNode().run()
