import keyboard
from timer import resetTimer, setTimer
from config import _hotKey
from screen import screenOff


def hookCallback(x):
    # print(x)
    # print()
    resetTimer()


def hotkeyCallback():
    screenOff()


def monitorKeyboard():
    keyboard.add_hotkey(_hotKey, hotkeyCallback)
    keyboard.hook(hookCallback)
    # 按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件
    keyboard.wait()


if __name__ == "__main__":
    monitorKeyboard()
