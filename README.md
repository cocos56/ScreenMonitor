# ScreenMonitor

操作系统本身有一套自动息屏机制，但这有时候会被一些第三方的程序破坏掉，比如摄像机程序会阻止系统自动息屏，导致屏幕一直亮着，很难受，所以就开发了这款软件。

默认情况下：超过5分钟不动鼠标和键盘会自动息屏并关闭声音，之后晃动鼠标或者点击键盘，会自动亮屏（由操作系统实现）并打开声音
如需修改超时时间，进入config.py修改_screenOffTimer变量即可

非Python程序员，如有这方面的需要，可以留言或者[联系我](https://coco56.gitee.io/blog/about)，我打包成exe程序，再开发一套图形界面。

# 程序入口

`screenMonitor.py`