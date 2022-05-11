from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

volume = cast(AudioUtilities.GetSpeakers().Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None),
              POINTER(IAudioEndpointVolume))


def setMute(flag=1):
    if volume.GetMute() == flag:
        return
    volume.SetMute(flag, None)


if __name__ == "__main__":
    setMute()
