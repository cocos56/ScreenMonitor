import keyboard
from timer import resetTimer, setTimer
from config import _hotKey, _screenOffTimer
from screen import screenOff
from time import sleep
from multThread import runThread, threadLock

_is_hotkey_pressed = False


def get_hotkey_status():
    return _is_hotkey_pressed


def set_hotkey_status(is_hotkey_pressed=False):
    global _is_hotkey_pressed
    threadLock.acquire()
    _is_hotkey_pressed = is_hotkey_pressed
    threadLock.release()


def hotkeyCallback():
    # print('hotkeyCallback')
    set_hotkey_status(True)
    runThread(after_press_hotkey)


def after_press_hotkey():
    sleep(0.5)
    # print('after_press_hotkey')
    screenOff(infoIndex=1)
    setTimer(_screenOffTimer)
    set_hotkey_status()


def onPressCallback(x):
    # print(x)
    if not get_hotkey_status():
        resetTimer()


def monitorKeyboard():
    keyboard.add_hotkey(_hotKey, hotkeyCallback)
    keyboard.on_press(onPressCallback)
    # 按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件
    keyboard.wait()


if __name__ == "__main__":
    monitorKeyboard()
