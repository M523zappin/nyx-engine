import os
import asyncio
import mmap
import sys
import socket
import json

class SovereignBrain:
    def __init__(self, path=os.path.expanduser("~/.nyx/memory.bin")):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
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
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)

    async def chat_loop(self):
        # Full-screen transition
        sys.stdout.write("\033[?1049h\033[?25h") 
        sys.stdout.flush()
        while self.running:
            sys.stdout.write("\033[H\033[2J")
            sys.stdout.write("\033[38;5;81mNYX-CAT // SOVEREIGN\033[0m\n")
            sys.stdout.write("─────────────────────────\n")
            sys.stdout.write(f"MEMORY: {self.brain.read()}\n\n")
            sys.stdout.write("Enter command: ")
            sys.stdout.flush()
            
            # Non-blocking input handling
            loop = asyncio.get_event_loop()
            cmd = await loop.run_in_executor(None, sys.stdin.readline)
            if cmd.strip():
                self.brain.write(cmd.strip())
            
            self.sock.sendto(json.dumps({"state": "active"}).encode(), ("127.0.0.1", 9999))

    async def run(self):
        await self.chat_loop()

if __name__ == "__main__":
    engine = NyxEngine()
    try: asyncio.run(engine.run())
    except KeyboardInterrupt: sys.stdout.write("\033[?1049l")
