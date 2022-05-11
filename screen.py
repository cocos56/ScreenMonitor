from ctypes import windll
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


def screenOff(infoIndex=0):
    """熄灭屏幕

    :param infoIndex: 访问info里的第几个元素，这个是最后为了显示通过什么方式熄灭屏幕的
    :return:
    """
    info = ['超时自动', '按键手动']
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                               SC_MONITORPOWER, MonitorPowerOff)

    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                          'USER32', '', SW_SHOW)
    setScreenStatus()
    setMute()
    print(f'{datetime.now()} {info[infoIndex]}熄灭屏幕，开启静音')


if __name__ == "__main__":
    screenOff()
