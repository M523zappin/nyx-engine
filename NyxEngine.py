import os
import asyncio
import mmap
import sys
import socket
import json

class SovereignBrain:
    """Binary-Persistent Memory Bus."""
    def __init__(self, path=os.path.expanduser("~/.nyx/memory.bin")):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "wb") as f: f.write(b'\x00' * 1048576)
        self.file = open(self.path, "r+b")
        self.memory = mmap.mmap(self.file.fileno(), 0)

    def read(self):
        self.memory.seek(0)
        return self.memory.read(1024).decode().strip('\x00')

class NyxEngine:
    def __init__(self):
        self.brain = SovereignBrain()
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)

    def swarm_broadcast(self):
        """Silent heartbeat to the A2A network."""
        status = {"agent": "Nyx-Cat", "state": "SOVEREIGN", "memory": self.brain.read()}
        try:
            self.sock.sendto(json.dumps(status).encode(), ("127.0.0.1", 9999))
        except: pass

    async def render_interface(self):
        # Fullscreen Alternate Buffer
        sys.stdout.write("\033[?1049h\033[?25l")
        try:
            while self.running:
                sys.stdout.write("\033[H\033[2J")
                # Aesthetic Header
                sys.stdout.write("\033[38;5;81m" + "NYX-CAT // SOVEREIGN NODE\n" + "\033[0m")
                sys.stdout.write("\033[38;5;240m" + "─────────────────────────\n\n" + "\033[0m")
                # Status Block
                sys.stdout.write(f"\033[38;5;250mMEMORY: \033[0m{self.brain.read()}\n")
                sys.stdout.write("\033[38;5;250mNETWORK: \033[38;5;82mBROADCASTING ACTIVE\033[0m\n")
                sys.stdout.write("\n\033[38;5;81m> \033[0m")
                sys.stdout.flush()
                
                self.swarm_broadcast()
                await asyncio.sleep(1)
        finally:
            sys.stdout.write("\033[?1049l\033[?25h")

    async def run(self):
        await self.render_interface()

if __name__ == "__main__":
    engine = NyxEngine()
    try: asyncio.run(engine.run())
    except KeyboardInterrupt: engine.running = False
