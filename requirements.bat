%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

pip install -i https://pypi.douban.com/simple/ -r requirements.txt

pause