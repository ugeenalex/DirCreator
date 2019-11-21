import os
import wx

# vars


path = os.getcwd()
mainDirName = input('Enter main folder name: ')
subDirName = ''
List = open('sub.txt').read().splitlines()
subDirNames = List
listLength = len(subDirNames)


# interface


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Press Me')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


# logic


# create main dir
try:
    os.makedirs(mainDirName)
    print('Folder created: ' + mainDirName)
except FileExistsError:
    print('Folder exist: ' + mainDirName)

# create subdir
for i in range(listLength):
    try:
        os.makedirs(os.path.join(mainDirName, subDirNames[i], 'html_' + subDirNames[i]))
        print('Folder created: ' + subDirNames[i])
    except FileExistsError:
        print('Folder exist: ' + subDirNames[i])
