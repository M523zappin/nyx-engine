import curses
import os
import mmap

class Brain:
    def __init__(self, path=os.path.expanduser("~/.nyx.bin")):
        if not os.path.exists(path):
            with open(path, "wb") as f: f.write(b'\x00' * 1024)
        self.mem = mmap.mmap(os.open(path, os.O_RDWR), 1024)
    def read(self):
        self.mem.seek(0); return self.mem.read(1024).decode().strip('\x00')
    def write(self, txt):
        self.mem.seek(0); self.mem.write(txt.encode().ljust(1024, b'\x00'))

def main(stdscr):
    brain = Brain()
    # Setup Colors
    curses.curs_set(1)
    stdscr.clear()
    
    while True:
        height, width = stdscr.getmaxyx()
        stdscr.clear()
        
        # Header // Styled
        stdscr.addstr(0, 0, "NYX // SOVEREIGN ENGINE", curses.A_BOLD)
        stdscr.addstr(1, 0, "-" * width)
        
        # Memory Bus // Centered-ish
        stdscr.addstr(3, 2, f"MEMORY: {brain.read()}")
        
        # Chat Box // Anchored to bottom
        stdscr.addstr(height-2, 0, "-" * width)
        stdscr.addstr(height-1, 0, "INPUT >> ")
        
        stdscr.refresh()
        
        # Capture input
        stdscr.echo()
        cmd = stdscr.getstr(height-1, 9, width-10).decode('utf-8')
        if cmd:
            brain.write(cmd)

if __name__ == "__main__":
    curses.wrapper(main)
