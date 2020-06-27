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
        print('距离息屏还有：%d秒' % (_screenOffTimer - _timer))
        if getTimer() > _screenOffTimer: screenOff()


def resetTimer():
    if getTimer() > 1:
        setTimer()
    if not getScreenStatus():
        setScreenStatus(True)
        setMute(0)
        print(datetime.now(), '关闭静音')

