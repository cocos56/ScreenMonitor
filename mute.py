from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import argparse

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))


def setMute(flag=1):
    if volume.GetMute() == flag:
        return
    volume.SetMute(flag, None)


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mute", help="Show the current version.",
                    action="store_true")

args = parser.parse_args()
if args.mute:
    print("The current version is v1.0")

if __name__ == "__main__":
    setMute()
