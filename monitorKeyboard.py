import keyboard
from timer import resetTimer, setTimer
from config import _screenOffTimer, _hotKey
from time import sleep
from multThread import runThread


def hookCallback(x):
    # print(x)
    # print()
    resetTimer()


def setT():
    setTimer(_screenOffTimer)
    print('通过热键：', _hotKey, '息屏', sep='')


def hotkeyCallback():
    runThread(setT, 0.5)


def monitorKeyboard():
    keyboard.add_hotkey(_hotKey, hotkeyCallback)
    keyboard.hook(hookCallback)
    # 按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件
    keyboard.wait()


if __name__ == "__main__":
    monitorKeyboard()
