import os
import time
import sys

def prowl():
    print("\x1b[?1049h\x1b[?25l") # Ghost Buffer
    try:
        while True:
            # Clear UI and update
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" NYX-CAT [SOVEREIGN] | " + time.strftime("%H:%M:%S"))
            print("═" * 40)
            print("\n 🗨  Nyx-Cat Prowling... 🐾\n")
            print("─" * 40)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\x1b[?1049l\x1b[?25h") # Exit Buffer

if __name__ == "__main__":
    prowl()
