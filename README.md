# selenium
selenium学习库
#### Q1: windows系统使用cmd可以直接运webdriver，但是通过pycharm中的代码执行就提示找不到系统文件，报错如下：
（前提是我的webdriver配置不是和放在python放在同一目录下，是单独放在`C:\Program Files\selenium-webdriver）` 而python安装在`C:\python3.7`
`C:\python3.7\python.exe D:/workspace/selenium/demo01.py
Traceback (most recent call last):
  File "C:\python3.7\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "C:\python3.7\lib\subprocess.py", line 800, in __init__
    restore_signals, start_new_session)
  File "C:\python3.7\lib\subprocess.py", line 1207, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] 系统找不到指定的文件。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:/workspace/selenium/demo01.py", line 42, in <module>
    case = TestCase()
  File "D:/workspace/selenium/demo01.py", line 19, in __init__
    self.driver = webdriver.Chrome()
  File "C:\python3.7\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 73, in __init__
    self.service.start()
  File "C:\python3.7\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home


Process finished with exit code 1
`

- A1: 暂时解决办法就是把webdriver 的文件移动到了python的安装目录下就没问题了。