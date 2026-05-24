import os
import asyncio
import mmap
import sys
import socket
import json
import selectors

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
        self.selector = selectors.DefaultSelector()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)
        self.selector.register(self.sock, selectors.EVENT_READ)

    def swarm_broadcast(self):
        """Broadcast status via non-blocking socket."""
        status = {"agent": "Nyx-Cat", "state": "SOTA-ACTIVE", "memory": self.brain.read()}
        self.sock.sendto(json.dumps(status).encode(), ("127.0.0.1", 9999))

    async def render_tui(self):
        sys.stdout.write("\033[?1049h\033[?25l")
        try:
            while self.running:
                sys.stdout.write("\033[H\033[2J")
                sys.stdout.write("NYX-CAT: SOTA SWARM NODE | ARCHITECTURE: ASYNC-SELECTORS\n")
                sys.stdout.write("=========================================================\n")
                sys.stdout.write(f"SYSTEM: {self.brain.read()}\n")
                sys.stdout.write("STATUS: BROADCASTING & MONITORING\n")
                sys.stdout.flush()
                await asyncio.sleep(0.5)
        finally:
            sys.stdout.write("\033[?1049l\033[?25h")

    async def run(self):
        loop = asyncio.get_event_loop()
        # Schedule the broadcast independently of the UI
        while self.running:
            self.swarm_broadcast()
            await asyncio.sleep(1)

if __name__ == "__main__":
    engine = NyxEngine()
    try: asyncio.run(engine.run())
    except KeyboardInterrupt: engine.running = False
