import os
import asyncio
import mmap
import sys
import time

class SovereignBrain:
    """Memory-mapped binary persistence layer for agent state."""
    def __init__(self, path=os.path.expanduser("~/.nyx.bin")):
        self.path = path
        # Ensure memory bus exists
        if not os.path.exists(self.path):
            with open(self.path, "wb") as f:
                f.write(b'\x00' * 1024)
        self.file = open(self.path, "r+b")
        self.memory = mmap.mmap(self.file.fileno(), 0)

    def write(self, data: str):
        self.memory.seek(0)
        # Wipe and update memory buffer
        self.memory.write(data.encode().ljust(1024, b'\x00'))

    def read(self):
        self.memory.seek(0)
        return self.memory.read(1024).decode().strip('\x00')

class NyxEngine:
    """Pulse-enabled, asynchronous sovereign interface."""
    def __init__(self):
        self.brain = SovereignBrain()

    async def render_loop(self):
        """Displays the pulsed dashboard."""
        sys.stdout.write("\033[?1049h\033[?25l")  # Fullscreen buffer
        try:
            while True:
                # Calculate rhythmic pulse intensity (ANSI 51-51)
                pulse = int(51 * (0.5 + 0.5 * (time.time() % 2)))
                sys.stdout.write(f"\033[H\033[2J")
                sys.stdout.write(f"\033[38;5;{pulse}m╔═════════════════════════════╗\n")
                sys.stdout.write("║ NYX // SOVEREIGN INTELLIGENCE ║\n")
                sys.stdout.write("╚═════════════════════════════╝\033[0m\n\n")
                sys.stdout.write(f"MEMORY BUS >> {self.brain.read()}\n\n")
                sys.stdout.write("\033[38;5;240m[INPUT_STREAM] > \033[0m")
                sys.stdout.flush()
                await asyncio.sleep(0.1)
        finally:
            sys.stdout.write("\033[?1049l\033[?25h")

    async def input_loop(self):
        """Handles non-blocking conversational input."""
        loop = asyncio.get_event_loop()
        while True:
            cmd = await loop.run_in_executor(None, sys.stdin.readline)
            if cmd.strip():
                # Process and commit to the binary brain
                self.brain.write(f"PROCESSED: '{cmd.strip()[:15]}...'")

    async def run(self):
        """Orchestrates concurrent pulse rendering and input listening."""
        await asyncio.gather(self.render_loop(), self.input_loop())

if __name__ == "__main__":
    try:
        engine = NyxEngine()
        asyncio.run(engine.run())
    except KeyboardInterrupt:
        sys.exit(0)
