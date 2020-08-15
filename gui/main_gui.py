import wx
from gui.home_tab import HomeTab


class MainFrame(wx.Frame):
    def __init__(self, title, size):
        super().__init__(parent=None, title=title, size=size)

        tabs = wx.Notebook(self)
        home = HomeTab(tabs)

        tabs.AddPage(home, 'Home')

        self.Show()
