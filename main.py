import wx
from gui.main_gui import MainFrame

from twisted.internet import wxreactor
wxreactor.install()
from twisted.internet import reactor

if __name__ == '__main__':
    app_instance = wx.App()
    app_size = wx.Size(800, 600)
    main_frame = MainFrame('MC Bot Manager', app_size)
    reactor.registerWxApp(app_instance)
    reactor.run()
