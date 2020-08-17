import wx
from gui.home_tab import HomeTab


class MainFrame(wx.Frame):
    def __init__(self, title, size):
        super().__init__(parent=None, title=title, size=size)

        tabs = wx.Notebook(self)
        home = HomeTab(tabs)

        tabs.AddPage(home, 'Home')

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    app_size = wx.Size(800, 600)
    frame = MainFrame('test', app_size)
    app.MainLoop()
