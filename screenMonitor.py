from multThread import runThread
from monitorMouse import monitorMouse
from monitorKeyboard import monitorKeyboard
from timer import updateTimer
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="Show the current version.",
                    action="store_true")

args = parser.parse_args()
if args.mute:
    print("The current version is v0.0.1")
    exit(0)


if __name__ == "__main__":
    runThread(monitorMouse)
    runThread(monitorKeyboard)
    runThread(updateTimer)
