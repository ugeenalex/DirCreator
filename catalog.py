import os
import wx


app = wx.App()
frame = wx.Frame(parent=None, title='Directory Creator')
frame.Show()
app.MainLoop()

path = os.getcwd()
mainDirName = input('Enter main folder name: ')
subDirName = ''
List = open('sub.txt').read().splitlines()
subDirNames = List
listLength = len(subDirNames)

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
