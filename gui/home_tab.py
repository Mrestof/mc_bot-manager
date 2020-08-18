import wx
import wx.adv


class HomeTab(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.available_mods = ('Send once', 'Repeat message')
        self.bot_selectors = ['All']

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # add "Chat:" title in top of the page
        chat_title = wx.StaticText(self, label='Chat:')
        main_sizer.Add(chat_title, flag=wx.ALL, border=10)

        # add field with messages from minecraft server
        self.message_field = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE)
        main_sizer.Add(self.message_field, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        # add selection of msg mode and bots to send msg
        base_settings_sizer = wx.BoxSizer()

        chat_mode_title = wx.StaticText(self, label='Chat Mode:')
        self.chat_mode_choice = wx.Choice(self, choices=self.available_mods)
        self.chat_mode_choice.SetSelection(0)
        bot_selector_title = wx.StaticText(self, label='Bot Selector:')
        self.bot_selector_choice = wx.Choice(self, choices=self.bot_selectors)
        self.bot_selector_choice .SetSelection(0)

        base_settings_sizer.Add(chat_mode_title, flag=wx.RIGHT | wx.ALIGN_CENTER, border=10)
        base_settings_sizer.Add(self.chat_mode_choice, proportion=1)
        base_settings_sizer.Add(bot_selector_title, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER, border=10)
        base_settings_sizer.Add(self.bot_selector_choice, proportion=1)

        main_sizer.Add(base_settings_sizer, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        # add big panel to set detail configurations and to control the state of bots
        more_control_sizer = wx.BoxSizer()
        settings_sizer = wx.BoxSizer(wx.VERTICAL)
        control_sizer = wx.BoxSizer(wx.VERTICAL)
        td_bot_sizer = wx.BoxSizer()
        td_iter_sizer = wx.BoxSizer()
        repeats_sizer = wx.BoxSizer()

        # building side with settings
        td_bot_title = wx.StaticText(self, label='Time delay between each bot message (time in milliseconds) :')
        td_iter_title = wx.StaticText(self, label='Time delay between iterations (time in milliseconds) :')
        repeats_title = wx.StaticText(self, label='Number of message repeats (if 0, repeat infinitely) :')

        self.td_bot_spin = wx.SpinCtrl(self, max=3600*1000)
        self.td_iter_spin = wx.SpinCtrl(self, value='5000', max=3600*1000)
        self.repeats_spin = wx.SpinCtrl(self, max=9999999)

        td_bot_sizer.Add(td_bot_title, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER, border=10)
        td_bot_sizer.Add(self.td_bot_spin, 1, wx.RIGHT, 10)
        td_iter_sizer.Add(td_iter_title, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER, border=10)
        td_iter_sizer.Add(self.td_iter_spin, 1, wx.RIGHT, 10)
        repeats_sizer.Add(repeats_title, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER, border=10)
        repeats_sizer.Add(self.repeats_spin, 1, wx.RIGHT, 10)

        settings_sizer.Add(td_bot_sizer, flag=wx.EXPAND | wx.BOTTOM, border=11)
        settings_sizer.Add(td_iter_sizer, flag=wx.EXPAND | wx.BOTTOM, border=11)
        settings_sizer.Add(repeats_sizer, flag=wx.EXPAND | wx.BOTTOM, border=11)

        # building side with control buttons
        self.start_btn = wx.Button(self, label='Send')
        self.run_control_btn = wx.Button(self, label='Pause')
        self.stop_btn = wx.Button(self, label='Stop')

        control_sizer.Add(self.start_btn, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.BOTTOM, border=10)
        control_sizer.Add(self.run_control_btn, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.BOTTOM, border=10)
        control_sizer.Add(self.stop_btn, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.BOTTOM, border=10)

        more_control_sizer.Add(settings_sizer, proportion=7)
        more_control_sizer.Add(control_sizer, proportion=3)
        main_sizer.Add(more_control_sizer, flag=wx.EXPAND)

        # add a message input field to the bottom
        self.msg_input = wx.TextCtrl(self)
        self.msg_input.SetHint('Enter your message here')
        main_sizer.Add(self.msg_input, flag=wx.EXPAND)

        self.SetSizer(main_sizer)
