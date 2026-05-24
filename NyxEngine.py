import os, asyncio, mmap, sys

class Brain:
    def __init__(self, path=os.path.expanduser("~/.nyx.bin")):
        if not os.path.exists(path):
            with open(path, "wb") as f: f.write(b'\x00' * 1024)
        self.mem = mmap.mmap(os.open(path, os.O_RDWR), 1024)
    def read(self):
        self.mem.seek(0); return self.mem.read(1024).decode().strip('\x00')
    def write(self, txt):
        self.mem.seek(0); self.mem.write(txt.encode().ljust(1024, b'\x00'))

async def main():
    brain = Brain()
    # INITIALIZATION: Set background to deep black/navy (ANSI 0;38;5;232)
    # This overrides the default terminal look-and-feel.
    sys.stdout.write("\033[?1049h\033[48;5;232m\033[38;5;15m\033[2J")
    
    try:
        while True:
            rows, cols = os.get_terminal_size()
            sys.stdout.write("\033[H")
            # Minimalist, clean headers
            sys.stdout.write("\033[1mNYX // SOVEREIGN ENGINE\033[0m\n")
            sys.stdout.write(f"MEMORY: {brain.read()}\n")
            
            # Draw persistent input area
            sys.stdout.write(f"\033[{rows};1H\033[48;5;235m") # Subtle grey footer
            sys.stdout.write(" INPUT >> ")
            sys.stdout.flush()
            
            cmd = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
            if cmd.strip():
                brain.write(cmd.strip())
                # Clear chat input line efficiently
                sys.stdout.write(f"\033[{rows};1H\033[K")
    finally:
        sys.stdout.write("\033[0m\033[?1049l")

if __name__ == "__main__":
    asyncio.run(main())
