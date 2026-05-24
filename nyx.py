import os, asyncio, mmap, sys, time

class NyxBrain:
    def __init__(self):
        self.mem = mmap.mmap(os.open(os.path.expanduser("~/.nyx.bin"), os.O_CREAT|os.O_RDWR), 1024)
    def update(self, txt): 
        self.mem.seek(0); self.mem.write(txt.encode().ljust(1024, b'\x00'))
    def read(self): 
        self.mem.seek(0); return self.mem.read(1024).decode().strip('\x00')

async def nyx_core():
    brain = NyxBrain()
    sys.stdout.write("\033[?1049h\033[?25h") # Enter Fullscreen, Show Cursor
    try:
        while True:
            # Rhythmic Visual Identity
            sys.stdout.write(f"\033[H\033[2J\033[38;5;{int(51*(0.5+0.5*(time.time()%2)))}m╔═════════════════════════════╗\n║ NYX // SOVEREIGN INTELLIGENCE ║\n╚═════════════════════════════╝\033[0m\n\n")
            sys.stdout.write(f"LAST THOUGHT: {brain.read()}\n\n> ")
            sys.stdout.flush()
            
            # Intelligent Input Handling
            loop = asyncio.get_event_loop()
            cmd = await loop.run_in_executor(None, sys.stdin.readline)
            if cmd.strip():
                # Logic Layer: Process input and store in binary brain
                response = f"Acknowledged: '{cmd.strip()[:20]}...'. Processing Sovereign directive."
                brain.update(response)
    finally: sys.stdout.write("\033[?1049l")

if __name__ == "__main__": asyncio.run(nyx_core())
