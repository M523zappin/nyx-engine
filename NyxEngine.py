import os, mmap, sys, time

class Brain:
    def __init__(self, path=os.path.expanduser("~/.nyx.bin")):
        if not os.path.exists(path):
            with open(path, "wb") as f: f.write(b'\x00' * 2048)
        self.mem = mmap.mmap(os.open(path, os.O_RDWR), 2048)
    def read(self):
        self.mem.seek(0); return self.mem.read(2048).decode().strip('\x00')
    def write(self, txt):
        self.mem.seek(0); self.mem.write(txt.encode().ljust(2048, b'\x00'))

def main():
    brain = Brain()
    # Force Alternate Buffer (Full Screen Takeover)
    sys.stdout.write("\033[?1049h\033[2J")
    
    try:
        while True:
            # Get terminal dimensions for clean layout
            try:
                rows, cols = os.get_terminal_size()
            except:
                rows, cols = 24, 80
            
            # Draw UI
            sys.stdout.write(f"\033[H\033[1;36mNYX // SOVEREIGN NODE\033[0m\n")
            sys.stdout.write(f"LOG: {brain.read()}\n")
            
            # Draw Input Bar at Bottom
            sys.stdout.write(f"\033[{rows};1H\033[47;30m CHAT >> \033[0m ")
            sys.stdout.flush()
            
            # Simple, non-blocking input
            cmd = sys.stdin.readline().strip()
            if cmd:
                brain.write(f"NYX: '{cmd}' PROCESSED.")
    finally:
        sys.stdout.write("\033[?1049l")

if __name__ == "__main__":
    main()
