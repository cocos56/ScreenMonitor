import pywintypes
import win32gui

full_screen_rectangles = [(0, 0, 1536, 864), (-1, -1, 1537, 865)]
_excluded_programs = [{'name': '铁甲雄兵', 'classname': 'TNG8SK2K8E', 'title': '铁甲雄兵'},
                      {'name': '哔哩哔哩', 'classname': 'Chrome_WidgetWin_1', 'title': '哔哩哔哩'}]


def is_current_window_excluded_program():
    current_window = win32gui.GetForegroundWindow()
    try:
        classname = win32gui.GetClassName(current_window)
        title = win32gui.GetWindowText(current_window)
        for i in _excluded_programs:
            if i['classname'] == classname and i['title'] in title \
                    and win32gui.GetWindowRect(current_window) in full_screen_rectangles:
                print(f'{i["name"]}正在阻止息屏')
                return True
    except pywintypes.error as e:
        print(e)
    return False
