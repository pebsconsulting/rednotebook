#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Aug 26 02:37:41 2008

import wx, datetime, wx.calendar
from wx.lib.wordwrap import wordwrap

from diaryGui import DiaryCalendar
from contentTree import ContentTree

# begin wxGlade: extracode
# end wxGlade




class MainPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainPanel.__do_layout
        pass
        # end wxGlade

# end of class MainPanel


class MainFrame(wx.Frame):
    def __init__(self, redNotebook, *args, **kwds):
        self.redNotebook = redNotebook
        
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.window_1 = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_1_pane_2 = wx.Panel(self.window_1, -1)
        self.window_2 = wx.SplitterWindow(self.window_1_pane_2, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_2_pane_2 = wx.Panel(self.window_2, -1)
        self.window_2_pane_1 = wx.Panel(self.window_2, -1)
        self.window_1_pane_1 = wx.Panel(self.window_1, -1)
        
        # Menu Bar
        self.mainFrame_menubar = wx.MenuBar()
        global ID_ABOUT; ID_ABOUT = wx.ID_ABOUT
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_SAVE, "&Save", "Save all contents", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_DUPLICATE, "Backup", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_EXIT, "Exit", "Close the application", wx.ITEM_NORMAL)
        self.mainFrame_menubar.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_BACKWARD, "&Backward\tCtrl+B", "Go To Previous Day", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_FORWARD, "&Forward\tCtrl+F", "Go To Next Day", wx.ITEM_NORMAL)
        self.mainFrame_menubar.Append(wxglade_tmp_menu, "&Navigate")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_ABOUT, "&About", "Show information about the application", wx.ITEM_NORMAL)
        self.mainFrame_menubar.Append(wxglade_tmp_menu, "&Help")
        self.SetMenuBar(self.mainFrame_menubar)
        # Menu Bar end
        self.mainFrame_statusbar = self.CreateStatusBar(1, wx.ST_SIZEGRIP)
        
        # Tool Bar
        self.mainFrame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.mainFrame_toolbar)
        self.mainFrame_toolbar.AddLabelTool(wx.ID_SAVE, "Save", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.calendar = DiaryCalendar(self.window_1_pane_1, -1, style=wx.calendar.CAL_MONDAY_FIRST)
        self.buttonPrevDay = wx.Button(self.window_1_pane_1, wx.ID_BACKWARD, "")
        self.buttonNextDay = wx.Button(self.window_1_pane_1, wx.ID_FORWARD, "")
        self.buttonToday = wx.Button(self.window_1_pane_1, -1, "&Today")
        self.mainTextField = wx.TextCtrl(self.window_2_pane_1, -1, "", style=wx.TE_PROCESS_TAB|wx.TE_MULTILINE|wx.TE_WORDWRAP)
        self.contentTree = ContentTree(self.window_2_pane_2, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_EDIT_LABELS|wx.TR_HIDE_ROOT|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.onSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.onBackup, id=wx.ID_DUPLICATE)
        self.Bind(wx.EVT_MENU, self.onExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onButtonPrevDay, id=wx.ID_BACKWARD)
        self.Bind(wx.EVT_MENU, self.onButtonNextDay, id=wx.ID_FORWARD)
        self.Bind(wx.EVT_MENU, self.onAbout, id=ID_ABOUT)
        self.Bind(wx.EVT_BUTTON, self.onButtonPrevDay, self.buttonPrevDay)
        self.Bind(wx.EVT_BUTTON, self.onButtonNextDay, self.buttonNextDay)
        self.Bind(wx.EVT_BUTTON, self.onButtonToday, self.buttonToday)
        # end wxGlade
            
        #rausgenommen, da immer das D von CHANGED weggelassen wird
        self.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.onDateChange, self.calendar)
        self.calendar.SetHolidayColours('RED', 'WHITE')
        
        #Catch closing of frame
        self.Bind(wx.EVT_CLOSE, self.onClose)
        
        #Timer
        ID_TIMER = 1#wx.ID_ANY
        self.timer = wx.Timer(self, ID_TIMER)
        self.timerRound = 0
        self.Bind(wx.EVT_TIMER, self.OnTimer, id=ID_TIMER)


    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("The Red Notebook")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("../../icons/redNotebook-16.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((1014, 748))
        self.mainFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        mainFrame_statusbar_fields = [""]
        for i in range(len(mainFrame_statusbar_fields)):
            self.mainFrame_statusbar.SetStatusText(mainFrame_statusbar_fields[i], i)
        self.mainFrame_toolbar.Realize()
        self.window_1.SetMinimumPaneSize(256)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(self.calendar, 0, 0, 0)
        sizer_5.Add(self.buttonPrevDay, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_5.Add(self.buttonNextDay, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_6.Add(sizer_5, 0, 0, 0)
        sizer_7.Add(self.buttonToday, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_6)
        sizer_3.Add(self.mainTextField, 1, wx.EXPAND, 0)
        self.window_2_pane_1.SetSizer(sizer_3)
        sizer_4.Add(self.contentTree, 1, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        self.window_2_pane_2.SetSizer(sizer_4)
        self.window_2.SplitVertically(self.window_2_pane_1, self.window_2_pane_2, 513)
        sizer_2.Add(self.window_2, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_2)
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 256)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade
        
    

    def onDateChange(self, event): # wxGlade: MainFrame.<event_handler>
        newDate = self.calendar.PyGetDate()
        self.redNotebook.changeDate(newDate)
        event.Skip()

    def onSave(self, event): # wxGlade: MainFrame.<event_handler>
        self.redNotebook.saveToDisk()
        event.Skip()
        
    def onAbout(self,event): # wxGlade: MainFrame.<event_handler>    
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = "The Red Notebook"
        info.Version = self.redNotebook.version
        info.Copyright = "(C) 2008 Jendrik Seipp"
        info.Description = wordwrap(
            "A simple diary application.", 
            350, wx.ClientDC(self.window_1_pane_1)) # change the wx.ClientDC to use self.panel instead of self
        info.WebSite = ("http://sourceforge.net/projects/rednotebook/", "Red Notebook Website")
        info.Developers = ["Jendrik Seipp"]
        
        licenseText = "http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt"

        # change the wx.ClientDC to use self.panel instead of self
        info.License = wordwrap(licenseText, 500, wx.ClientDC(self.window_1_pane_1))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)
        
    def onExit(self, event): # wxGlade: MainFrame.<event_handler>
        self.Close(True)  # Close the frame.
        event.Skip()

    def onClose(self, event): # wxGlade: MainFrame.<event_handler>
        #TODO: Uncomment
        #dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
         #   wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        #ret = dial.ShowModal()
        #if ret == wx.ID_YES:
            self.redNotebook.saveToDisk()
            self.Destroy()
        #else:
          #  event.Veto()

    def onWebsite(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onWebsite' not implemented"
        event.Skip()
        
    def showDay(self, day):
        self.contentTree.clear()
        self.mainTextField.SetValue(day.text)
        self.contentTree.addDayContent(day)
        self.contentTree.ExpandAll()
        
    def getDayText(self):
        return self.mainTextField.GetValue()
    
    def showMessageInStatusBar(self, messageText):
        self.setStatusBarText(messageText)
        #start timer. The timer raises a Timer event every 50 ms and OnTimer is called
        self.timer.Start(50)
        
    def OnTimer(self, event):
        self.timerRound += 1
        if self.timerRound == 30:
            #self.statusbar.SetBackgroundColour('#E0E2EB')
            self.setStatusBarText('')
            self.timer.Stop()
            self.timerRound = 0
            
    def setStatusBarText(self, text):
        self.mainFrame_statusbar.SetStatusText(text, 0)
        self.mainFrame_statusbar.Refresh()

    def onButtonToday(self, event): # wxGlade: MainFrame.<event_handler>
        actualDate = datetime.date.today()
        self.redNotebook.changeDate(actualDate)
        event.Skip()

    def onButtonPrevDay(self, event): # wxGlade: MainFrame.<event_handler>
        self.redNotebook.goToPrevDay()
        event.Skip()

    def onButtonNextDay(self, event): # wxGlade: MainFrame.<event_handler>
        self.redNotebook.goToNextDay()
        event.Skip()

    def onButtonPrevEditedDay(self, event): # wxGlade: MainFrame.<event_handler>
        self.redNotebook.goToPrevEditedDay()
        event.Skip()

    def onButtonLastEntry(self, event): # wxGlade: MainFrame.<event_handler>
        self.onButtonToday(event)
        self.redNotebook.goToNextDay()
        self.redNotebook.goToPrevEditedDay()
        event.Skip()

    def onButtonNextEditedDay(self, event): # wxGlade: MainFrame.<event_handler>
        self.redNotebook.goToNextEditedDay()
        event.Skip()

    

    def onBackup(self, event): # wxGlade: MainFrame.<event_handler>
        self.redNotebook.backupContents()
        event.Skip()

# end of class MainFrame

#if __name__ == "__main__":
#    app = wx.PySimpleApp(0)
#    wx.InitAllImageHandlers()
#    mainFrame = MainFrame(None, -1, "")
#    app.SetTopWindow(mainFrame)
#    mainFrame.Show()
#    app.MainLoop()

