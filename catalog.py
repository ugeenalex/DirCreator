import os

path = os.getcwd()
mainDirName = input('Enter main folder name: ')
subDirName = ''
List = open('sub.txt').read().splitlines()
subDirNames = List
listLength = len(subDirNames)

# create main derictory
try:
    os.makedirs(mainDirName)
    print('Folder created: ' + mainDirName)
except FileExistsError:
    print('Folder exist: ' + mainDirName)

# subdirs
for i in range(listLength):
    try:
        os.makedirs(os.path.join(mainDirName, subDirNames[i], 'html_' + subDirNames[i]))
        print('Folder created: ' + subDirNames[i])
    except FileExistsError:
        print('Folder exist: ' + subDirNames[i])