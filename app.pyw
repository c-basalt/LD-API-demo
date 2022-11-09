import wx
import threading

from frame.main import MainFrame
from utils import local_api

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    threading.Thread(target=local_api.app.run, kwargs={"host": '127.0.0.1', "port": 8745}, daemon=True).start()
    app.MainLoop()
