import os, mmap, sys, ast

class Sentinel:
    """The Gatekeeper: Ensures core integrity before execution."""
    ALLOWED = {'os', 'mmap', 'sys', 'ast'}
    
    @staticmethod
    def verify():
        with open(__file__, "r") as f:
            tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name not in Sentinel.ALLOWED:
                            return False
        return True

def run():
    # Health Check
    if not Sentinel.verify():
        print("CRITICAL: Integrity breach detected in source. Reverting to safe mode.")
        sys.exit(1)
        
    # Execution
    sys.stdout.write("\033[?1049h\033[2J")
    try:
        while True:
            # Main UI Loop
            rows, cols = os.get_terminal_size()
            sys.stdout.write(f"\033[H\033[1;36mNYX // SOVEREIGN NODE // STATUS: SECURE\033[0m\n")
            sys.stdout.write(f"\033[{rows};1H\033[47;30m CHAT >> \033[0m ")
            sys.stdout.flush()
            
            cmd = sys.stdin.readline().strip()
            if cmd.lower() == "exit": break
    finally:
        sys.stdout.write("\033[?1049l")

if __name__ == "__main__": run()
