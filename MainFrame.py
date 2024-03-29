import wx
import os
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''
        wx.Frame.__init__(self, parent, title=title, size=(1,1))
        self.control = wx.TextCtrl(self, style=wx.ACCEL_CTRL)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Input","Open a file to edit")
       # menuInput = filemenu.Append(wx.ID_INPUT,"&Input","Input your command")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Information about this progarm")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnOpen,menuOpen)
        #self.Bind(wx.EVT_MENU,self.OnInPut,menuInput)
        self.Bind(wx.EVT_MENU,self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU,self.OnAbout, menuAbout)

        #self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        #self.buttons = []
        #for i in range(0,6):
        #    self.buttons.append(wx.Button(self, -1, "Button &"+ str(i)))
        #    self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        #self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "A sample editor \n in wxPython","Introduction", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,e):
        self.Close(True)

    def OnOpen(self,e):
        """Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname,"", "*.*",wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None,"Sample editor")
app.MainLoop()