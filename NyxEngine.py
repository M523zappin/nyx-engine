import os
import asyncio
import mmap
import sys

class SovereignBrain:
    def __init__(self, path=os.path.expanduser("~/.nyx/memory.bin")):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        # Allocate 1MB for the binary index
        if not os.path.exists(self.path):
            with open(self.path, "wb") as f: f.write(b'\x00' * 1048576)
        self.file = open(self.path, "r+b")
        self.memory = mmap.mmap(self.file.fileno(), 0)

    def write(self, data: str):
        self.memory.seek(0)
        self.memory.write(data.encode().ljust(1024, b'\x00'))

    def read(self):
        self.memory.seek(0)
        return self.memory.read(1024).decode().strip('\x00')

class NyxEngine:
    def __init__(self):
        self.brain = SovereignBrain()
        self.running = True

    async def render_tui(self):
        # Enter alternate screen buffer and hide cursor
        sys.stdout.write("\033[?1049h\033[?25l")
        sys.stdout.flush()
        try:
            while self.running:
                sys.stdout.write("\033[H\033[2J") # Clear screen
                sys.stdout.write("NYX-CAT: SOVEREIGN INTELLIGENCE ACTIVE\n")
                sys.stdout.write("======================================\n")
                sys.stdout.write(f"MEMORY BUS: {self.brain.read()}\n")
                sys.stdout.write("STATUS: AWAITING SWARM INPUT...\n")
                sys.stdout.flush()
                await asyncio.sleep(0.5)
        finally:
            # Cleanup: restore screen and cursor
            sys.stdout.write("\033[?1049l\033[?25h")
            sys.stdout.flush()

    async def run(self):
        await self.render_tui()

if __name__ == "__main__":
    engine = NyxEngine()
    try:
        asyncio.run(engine.run())
    except KeyboardInterrupt:
        engine.running = False
