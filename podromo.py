""" 
 Pomodoro Focus Timer – Project 15
 User sets work minutes, short‑break minutes, long‑break minutes, and total rounds.
 Live countdown (mm:ss) shown in terminal.
 Plays a beep (cross‑platform) at each transition.
 Logs total focused minutes at the end.
"""
import time
import os
import sys
from datetime import datetime, timedelta

# ————— Utility Functions ————————————————————————————

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def beep():
    """Cross‑platform beep sound (fallback to print)."""
    try:
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 500)
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()
    except Exception:
        print("<ding>")


def countdown(minutes, label):
    seconds = minutes * 60
    end_time = datetime.now() + timedelta(seconds=seconds)
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{label} | {mins:02d}:{secs:02d}"
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    clear_screen()
    beep()
    print(f" {label} complete!        ")
    time.sleep(1)

# ————— Main Flow ————————————————————————————————

def main():
    clear_screen()
    print("  Pomodoro Focus Timer (Project 15)\n")

    try:
        work_min   = int(input("Work session (minutes, default 25): ") or 25)
        short_min  = int(input("Short break (minutes, default 5): ") or 5)
        long_min   = int(input("Long break (minutes, default 15): ") or 15)
        rounds     = int(input("Total rounds before long break (default 4): ") or 4)
    except ValueError:
        print(" Please enter numbers only. Restarting…")
        time.sleep(2)
        return main()

    total_focus = 0
    cycle = 0

    while True:
        cycle += 1
        # Work Session
        countdown(work_min, f"Focus {cycle}")
        total_focus += work_min

        # Decide which break
        if cycle % rounds == 0:
            countdown(long_min, "Long Break")
        else:
            countdown(short_min, "Short Break")

        # Ask user to continue or exit
        cont = input("Press [Enter] to start next session or type 'q' to quit: ").lower()
        if cont == 'q':
            break
        clear_screen()

    # Summary
    clear_screen()
    print(" Pomodoro session finished!")
    print(f"Total focused minutes: {total_focus}")
    print("Keep up the great work! ")


if __name__ == "__main__":
    main()
