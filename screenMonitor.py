from multThread import runThread
from monitorMouse import monitorMouse
from monitorKeyboard import monitorKeyboard
from timer import updateTimer

runThread(monitorMouse)
runThread(monitorKeyboard)
runThread(updateTimer)
