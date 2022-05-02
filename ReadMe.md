# 1. ScreenMonitor

操作系统本身有一套自动息屏机制，但这有时候会被一些第三方的程序破坏掉，比如火星安防监控程序会阻止系统自动息屏，导致屏幕一直亮着，很难受，所以就开发了这款软件。
另外操作系统只有一套自动息屏机制，如果我想在息屏的时候把电脑声音也关了怎么办呢？这时操作系统并没有为我们提供相关功能。

默认情况下：
* 超过5分钟不动鼠标和键盘会自动息屏并关闭电脑声音，之后晃动鼠标或者点击键盘，会自动亮屏（由操作系统实现）并打开声音，如需修改超时时间，进入`config.py`修改`_screenOffTimer`变量即可。
* 支持自定义快捷键，按alt键+英语字母表的第15个字母O键（不是数字零键）即可息屏并关闭电脑声音，如果需要修改快捷键，进入`config.py`修改`_hotKey`变量即可

非Python程序员，如有这方面的需要，可以留言或者[联系我](https://coco56.gitee.io/blog/about)，我打包成exe程序，再开发一套图形界面。另外如果仅仅想手动关闭屏幕，也可以参考下载并运行打包好的程序：[Windows 一键息屏程序ScreenOff下载及说明](https://coco56.blog.csdn.net/article/details/106956281)

目前仅在Windows 10上进行了测试，测试结果ojbk，没有任何问题，但无法保证在其他系统上也是ojbk的。

最后如果需要把软件设为开机自启，可以参考：[Windows通过修改注册表设置开机启动程序](https://coco56.blog.csdn.net/article/details/102493477)，修改screenMonitor.bat文件，然后将screenMonitor.bat加入到注册表中就行。

# 2. 程序入口

`screenMonitor.py`

# 3. 项目文档

* [https://coco56.blog.csdn.net/article/details/106975917](https://coco56.blog.csdn.net/article/details/106975917)

# 4. 参考

* [Python息屏、关闭显示器代码](https://coco56.blog.csdn.net/article/details/106964234)
* [python使用pycaw获取windows当前音量值以及调节音量、设置静音](https://coco56.blog.csdn.net/article/details/106962278)