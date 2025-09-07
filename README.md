Pomodoro Focus Timer (CLI)

A simple command-line Pomodoro timer that helps you stay focused and productive.
You can customize work sessions, short breaks, long breaks, and the number of rounds.
The timer runs live in the terminal with a countdown and plays a beep sound at each transition.

Features

Customizable:

Work session minutes (default 25)

Short break minutes (default 5)

Long break minutes (default 15)

Rounds before long break (default 4)

Live countdown timer (mm:ss) displayed in the terminal

Cross-platform beep notification at each transition

Logs total focused minutes at the end

Clean and simple command-line interface

Installation

No external libraries required – works with Python’s standard library.
Make sure you have Python 3 installed.

Clone or download this project and open the folder in your terminal.

Usage

Run the script from your terminal:

python podromo.py


You’ll be asked to input your session preferences. Example:

Pomodoro Focus Timer (Project 15)

Work session (minutes, default 25): 30
Short break (minutes, default 5): 10
Long break (minutes, default 15): 20
Total rounds before long break (default 4): 2


The timer will start and display a live countdown:

Focus 1 | 29:59


At the end of each session, a beep will play, and you’ll be prompted to continue or quit:

Focus 1 complete!
Press [Enter] to start next session or type 'q' to quit:

Example Run
Pomodoro Focus Timer (Project 15)

Work session (minutes, default 25):
Short break (minutes, default 5):
Long break (minutes, default 15):
Total rounds before long break (default 4):

Focus 1 | 24:59
...
Focus 1 complete!
Short Break | 04:59
...

Pomodoro session finished!
Total focused minutes: 75
Keep up the great work!

Notes

The beep works cross-platform (winsound on Windows, \a on Linux/macOS).

If sound is unavailable, a <ding> message is printed.

Screen auto-clears for a clean display between sessions.
