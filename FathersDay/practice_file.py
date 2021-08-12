import time
import webbrowser
import win32com.client as comctl
url = 'https://docs.google.com/presentation/d/1K-RNLdqdncs3JsoVbm_X5Hax-RCCL9lzhJgOn9ZFp9U/present'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

wsh = comctl.Dispatch("WScript.Shell")
# Google Chrome window title
wsh.AppActivate("icanhazip.com")
time.sleep(1)
wsh.SendKeys("{F11}")
