from ctypes import *
from datetime import datetime
from multThread import threadLock
from mute import setMute

HWND_BROADCAST = 0xffff
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MonitorPowerOff = 2
SW_SHOW = 5

_screenStatus = True


def getScreenStatus():
    return _screenStatus


def setScreenStatus(status=False):
    global _screenStatus
    threadLock.acquire()
    _screenStatus = status
    threadLock.release()


def screenOff():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                               SC_MONITORPOWER, MonitorPowerOff)

    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                          'USER32', '', SW_SHOW)
    setScreenStatus()
    setMute()
    print(datetime.now(), '开启静音，关闭屏幕')


if __name__ == "__main__":
    screenOff()
