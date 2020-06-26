import keyboard
from timer import resetTimer


def callback(x):
    # print(x)
    # print()
    resetTimer()


def monitorKeyboard():
    keyboard.hook(callback)
    # 按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件
    keyboard.wait()


if __name__ == "__main__":
    monitorKeyboard()
