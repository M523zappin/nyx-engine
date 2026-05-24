import os
import time

def prowl():
    # Clear the screen once at start
    os.system('cls')
    try:
        while True:
            # Move cursor to top-left instead of clearing to avoid flicker
            print("\033[H", end="")
            print(f" NYX-CAT [SOVEREIGN] | {time.strftime('%H:%M:%S')} ")
            print("═" * 50)
            print("\n 🗨  Nyx-Cat Prowling... 🐾\n")
            print("─" * 50)
            print("\n[Status: Autonomous & Active]")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting Sovereign State.")

if __name__ == "__main__":
    prowl()
