import os, mmap, sys

class Brain:
    def __init__(self, path=os.path.join(os.getcwd(), ".nyx.bin")):
        if not os.path.exists(path):
            with open(path, "wb") as f: f.write(b'\x00' * 4096)
        self.mem = mmap.mmap(os.open(path, os.O_RDWR), 4096)
    def read(self):
        self.mem.seek(0); return self.mem.read(4096).decode().strip('\x00')
    def write(self, txt):
        self.mem.seek(0); self.mem.write(txt.encode().ljust(4096, b'\x00'))

def run():
    brain = Brain()
    sys.stdout.write("\033[?1049h\033[2J") # Screen lock
    try:
        while True:
            rows, cols = os.get_terminal_size()
            sys.stdout.write(f"\033[H\033[1;36mNYX // SOVEREIGN NODE\033[0m\n")
            sys.stdout.write(f"MEM_BUS: {brain.read()}\n")
            sys.stdout.write(f"\033[{rows};1H\033[47;30m CHAT >> \033[0m ")
            sys.stdout.flush()
            
            cmd = sys.stdin.readline().strip()
            if cmd: brain.write(f"SYSTEM: '{cmd}' RECEIVED.")
    finally:
        sys.stdout.write("\033[?1049l")

if __name__ == "__main__": run()
