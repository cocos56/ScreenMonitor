from multThread import threadLock
from time import sleep
from mute import setMute
from datetime import datetime
from screen import screenOff, getScreenStatus, setScreenStatus
from config import _screenOffTimer

_timer = 0


def setTimer(timer=0):
    global _timer
    threadLock.acquire()
    _timer = timer
    threadLock.release()


def getTimer():
    return _timer


def updateTimer():
    while True:
        sleep(1)
        setTimer(getTimer() + 1)
        if not getScreenStatus():
            continue
        print(f'距离息屏还有：{_screenOffTimer - _timer}秒')
        if getTimer() > _screenOffTimer:
            screenOff()


def resetTimer():
    if getTimer() > 1:
        setTimer()
    if not getScreenStatus():
        setScreenStatus(True)
        # 当有鼠标或者键盘事件，操作系统会亮屏，所以只需要做一下取消静音就行了
        setMute(0)
        print(datetime.now(), '点亮屏幕，取消静音')
