import win32gui

_excluded_programs = [
    {
        'name': '铁甲雄兵',
        'classname': 'TNG8SK2K8E',
        'title': '铁甲雄兵',
    },
]


def is_current_window_excluded_program():
    current_window = win32gui.GetForegroundWindow()
    classname = win32gui.GetClassName(current_window)
    title = win32gui.GetWindowText(current_window)
    for i in _excluded_programs:
        if i['classname'] == classname and i['title'] == title:
            return True
    return False
