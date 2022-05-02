# 1. ScreenMonitor

操作系统本身有一套自动息屏机制，但这有时候会被一些第三方的程序破坏掉，比如火星安防监控程序会阻止系统自动息屏，导致屏幕一直亮着，很难受，所以就开发了这款软件。

默认情况下：超过5分钟不动鼠标和键盘会自动息屏并关闭声音，之后晃动鼠标或者点击键盘，会自动亮屏（由操作系统实现）并打开声音
如需修改超时时间，进入`config.py`修改`_screenOffTimer`变量即可

非Python程序员，如有这方面的需要，可以留言或者[联系我](https://coco56.gitee.io/blog/about)，我打包成exe程序，再开发一套图形界面。另外如果仅仅想手动关闭屏幕，也可以参考下载并运行打包好的程序：[Windows 一键息屏程序ScreenOff下载及说明](https://coco56.blog.csdn.net/article/details/106956281)

# 2. 程序入口

`screenMonitor.py`

# 3. 参考
* [Python息屏、关闭显示器代码](https://coco56.blog.csdn.net/article/details/106964234)
* [python使用pycaw获取windows当前音量值以及调节音量、设置静音](https://coco56.blog.csdn.net/article/details/106962278)