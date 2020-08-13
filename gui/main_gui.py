import wx


class MainFrame(wx.Frame):
    def __init__(self, title, size):
        super().__init__(parent=None, title=title, size=size)
        self.Show()
