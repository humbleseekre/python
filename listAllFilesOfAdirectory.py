#source: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
os.listdir() will get you everything that's in a directory - files and directories.

If you want just files, you could either filter this down using os.path:

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
    
    
Get a list of files with Python 2 and 3
os.listdir()
How to get all the files (and directories) in the current directory (Python 3)

Following, are simple methods to retrieve only files in the current directory, using os and the listdir() function, in Python 3. Further exploration, will demonstrate how to return folders in the directory, but you will not have the file in the subdirectory, for that you can use walk - discussed later).

 import os
 arr = os.listdir()
 print(arr)

 >>> ['$RECYCLE.BIN', 'work.txt', '3ebooks.txt', 'documents']
glob
I found glob easier to select the file of the same type or with something in common. Look at the following example:

import glob

txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)
glob with list comprehension
import glob

mylist = [f for f in glob.glob("*.txt")]
glob with a function
The function returns a list of the given extension (.txt, .docx ecc.) in the argument

import glob

def filebrowser(ext=""):
    "Returns files with an extension"
    return [f for f in glob.glob(f"*{ext}")]

x = filebrowser(".txt")
print(x)

>>> ['example.txt', 'fb.txt', 'intro.txt', 'help.txt']
glob extending the previous code
The function now returns a list of file that matched with the string you pass as argument

import glob

def filesearch(word=""):
    """Returns a list with all files with the word/extension in it"""
    file = []
    for f in glob.glob("*"):
        if word[0] == ".":
            if f.endswith(word):
                file.append(f)
                return file
        elif word in f:
            file.append(f)
            return file
    return file

lookfor = "example", ".py"
for w in lookfor:
    print(f"{w:10} found => {filesearch(w)}")
output

example    found => []
.py        found => ['search.py']
Getting the full path name with os.path.abspath
As you noticed, you don't have the full path of the file in the code above. If you need to have the absolute path, you can use another function of the os.path module called _getfullpathname, putting the file that you get from os.listdir() as an argument. There are other ways to have the full path, as we will check later (I replaced, as suggested by mexmex, _getfullpathname with abspath).

 import os
 files_path = [os.path.abspath(x) for x in os.listdir()]
 print(files_path)

 >>> ['F:\\documenti\applications.txt', 'F:\\documenti\collections.txt']
Get the full path name of a type of file into all subdirectories with walk
I find this very useful to find stuff in many directories, and it helped me find a file about which I didn't remember the name:

import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".docx"):
            print(os.path.join(r, file))
os.listdir(): get files in the current directory (Python 2)
In Python 2, if you want the list of the files in the current directory, you have to give the argument as '.' or os.getcwd() in the os.listdir method.

 import os
 arr = os.listdir('.')
 print(arr)

 >>> ['$RECYCLE.BIN', 'work.txt', '3ebooks.txt', 'documents']
To go up in the directory tree
# Method 1
x = os.listdir('..')

# Method 2
x= os.listdir('/')
Get files: os.listdir() in a particular directory (Python 2 and 3)
 import os
 arr = os.listdir('F:\\python')
 print(arr)

 >>> ['$RECYCLE.BIN', 'work.txt', '3ebooks.txt', 'documents']
Get files of a particular subdirectory with os.listdir()
import os

x = os.listdir("./content")
os.walk('.') - current directory
 import os
 arr = next(os.walk('.'))[2]
 print(arr)

 >>> ['5bs_Turismo1.pdf', '5bs_Turismo1.pptx', 'esperienza.txt']
next(os.walk('.')) and os.path.join('dir', 'file')
 import os
 arr = []
 for d,r,f in next(os.walk("F:\\_python")):
     for file in f:
         arr.append(os.path.join(r,file))

 for f in arr:
     print(files)

>>> F:\\_python\\dict_class.py
>>> F:\\_python\\programmi.txt
next(os.walk('F:\\') - get the full path - list comprehension
 [os.path.join(r,file) for r,d,f in next(os.walk("F:\\_python")) for file in f]

 >>> ['F:\\_python\\dict_class.py', 'F:\\_python\\programmi.txt']
os.walk - get full path - all files in sub dirs**
x = [os.path.join(r,file) for r,d,f in os.walk("F:\\_python") for file in f]
print(x)

>>> ['F:\\_python\\dict.py', 'F:\\_python\\progr.txt', 'F:\\_python\\readl.py']
os.listdir() - get only txt files
 arr_txt = [x for x in os.listdir() if x.endswith(".txt")]
 print(arr_txt)

 >>> ['work.txt', '3ebooks.txt']
Using glob to get the full path of the files
If I should need the absolute path of the files:

from path import path
from glob import glob
x = [path(f).abspath() for f in glob("F:\\*.txt")]
for f in x:
    print(f)

>>> F:\acquistionline.txt
>>> F:\acquisti_2018.txt
>>> F:\bootstrap_jquery_ecc.txt
Using os.path.isfile to avoid directories in the list
import os.path
listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
print(listOfFiles)

>>> ['a simple game.py', 'data.txt', 'decorator.py']
Using pathlib from Python 3.4
import pathlib

flist = []
for p in pathlib.Path('.').iterdir():
    if p.is_file():
        print(p)
        flist.append(p)

 >>> error.PNG
 >>> exemaker.bat
 >>> guiprova.mp3
 >>> setup.py
 >>> speak_gui2.py
 >>> thumb.PNG
With list comprehension:

flist = [p for p in pathlib.Path('.').iterdir() if p.is_file()]
Alternatively, use pathlib.Path() instead of pathlib.Path(".")

Use glob method in pathlib.Path()
import pathlib

py = pathlib.Path().glob("*.py")
for file in py:
    print(file)

>>> stack_overflow_list.py
>>> stack_overflow_list_tkinter.py
Get all and only files with os.walk
import os
x = [i[2] for i in os.walk('.')]
y=[]
for t in x:
    for f in t:
        y.append(f)
print(y)

>>> ['append_to_list.py', 'data.txt', 'data1.txt', 'data2.txt', 'data_180617', 'os_walk.py', 'READ2.py', 'read_data.py', 'somma_defaltdic.py', 'substitute_words.py', 'sum_data.py', 'data.txt', 'data1.txt', 'data_180617']
Get only files with next and walk in a directory
 import os
 x = next(os.walk('F://python'))[2]
 print(x)

 >>> ['calculator.bat','calculator.py']
Get only directories with next and walk in a directory
 import os
 next(os.walk('F://python'))[1] # for the current dir use ('.')

 >>> ['python3','others']
Get all the subdir names with walk
for r,d,f in os.walk("F:\\_python"):
    for dirs in d:
        print(dirs)

>>> .vscode
>>> pyexcel
>>> pyschool.py
>>> subtitles
>>> _metaprogramming
>>> .ipynb_checkpoints
os.scandir() from Python 3.5 and greater
import os
x = [f.name for f in os.scandir() if f.is_file()]
print(x)

>>> ['calculator.bat','calculator.py']

# Another example with scandir (a little variation from docs.python.org)
# This one is more efficient than os.listdir.
# In this case, it shows the files only in the current directory
# where the script is executed.

import os
with os.scandir() as i:
    for entry in i:
        if entry.is_file():
            print(entry.name)

>>> ebookmaker.py
>>> error.PNG
>>> exemaker.bat
>>> guiprova.mp3
>>> setup.py
>>> speakgui4.py
>>> speak_gui2.py
>>> speak_gui3.py
>>> thumb.PNG
Examples:
Ex. 1: How many files are there in the subdirectories?
In this example, we look for the number of files that are included in all the directory and its subdirectories.

import os

def count(dir, counter=0):
    "returns number of files in dir and subdirs"
    for pack in os.walk(dir):
        for f in pack[2]:
            counter += 1
    return dir + " : " + str(counter) + "files"

print(count("F:\\python"))

>>> 'F:\\\python' : 12057 files'
Ex.2: How to copy all files from a directory to another?
A script to make order in your computer finding all files of a type (default: pptx) and copying them in a new folder.

import os
import shutil
from path import path

destination = "F:\\file_copied"
# os.makedirs(destination)

def copyfile(dir, filetype='pptx', counter=0):
    "Searches for pptx (or other - pptx is the default) files and copies them"
    for pack in os.walk(dir):
        for f in pack[2]:
            if f.endswith(filetype):
                fullpath = pack[0] + "\\" + f
                print(fullpath)
                shutil.copy(fullpath, destination)
                counter += 1
    if counter > 0:
        print('-' * 30)
        print("\t==> Found in: `" + dir + "` : " + str(counter) + " files\n")

for dir in os.listdir():
    "searches for folders that starts with `_`"
    if dir[0] == '_':
        # copyfile(dir, filetype='pdf')
        copyfile(dir, filetype='txt')


>>> _compiti18\Compito Contabilità 1\conti.txt
>>> _compiti18\Compito Contabilità 1\modula4.txt
>>> _compiti18\Compito Contabilità 1\moduloa4.txt
>>> ------------------------
>>> ==> Found in: `_compiti18` : 3 files
Ex. 3: How to get all the files in a txt file
In case you want to create a txt file with all the file names:

import os
mylist = ""
with open("filelist.txt", "w", encoding="utf-8") as file:
    for eachfile in os.listdir():
        mylist += eachfile + "\n"
    file.write(mylist)
Example: txt with all the files of an hard drive
"""
We are going to save a txt file with all the files in your directory.
We will use the function walk()
"""

import os

# see all the methods of os
# print(*dir(os), sep=", ")
listafile = []
percorso = []
with open("lista_file.txt", "w", encoding='utf-8') as testo:
    for root, dirs, files in os.walk("D:\\"):
        for file in files:
            listafile.append(file)
            percorso.append(root + "\\" + file)
            testo.write(file + "\n")
listafile.sort()
print("N. of files", len(listafile))
with open("lista_file_ordinata.txt", "w", encoding="utf-8") as testo_ordinato:
    for file in listafile:
        testo_ordinato.write(file + "\n")

with open("percorso.txt", "w", encoding="utf-8") as file_percorso:
    for file in percorso:
        file_percorso.write(file + "\n")

os.system("lista_file.txt")
os.system("lista_file_ordinata.txt")
os.system("percorso.txt")
All the file of C:\ in one text file
This is a shorter version of the previous code. Change the folder where to start finding the files if you need to start from another position. This code generate a 50 mb on text file on my computer with something less then 500.000 lines with files with the complete path.

import os

with open("file.txt", "w", encoding="utf-8") as filewrite:
    for r, d, f in os.walk("C:\\"):
        for file in f:
            filewrite.write(f"{r + file}\n")
How to write a file with all paths in a folder of a type
With this function you can create a txt file that will have the name of a type of file that you look for (ex. pngfile.txt) with all the full path of all the files of that type. It can be useful sometimes, I think.

import os

def searchfiles(extension='.ttf', folder='H:\\'):
    "Create a txt file with all the file of a type"
    with open(extension[1:] + "file.txt", "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    filewrite.write(f"{r + file}\n")

# looking for png file (fonts) in the hard disk H:\
searchfiles('.png', 'H:\\')

>>> H:\4bs_18\Dolphins5.png
>>> H:\4bs_18\Dolphins6.png
>>> H:\4bs_18\Dolphins7.png
>>> H:\5_18\marketing html\assets\imageslogo2.png
>>> H:\7z001.png
>>> H:\7z002.png
(New) Find all files and open them with tkinter GUI
I just wanted to add in this 2019 a little app to search for all files in a dir and be able to open them by doubleclicking on the name of the file in the list. enter image description here

import tkinter as tk
import os

def searchfiles(extension='.txt', folder='H:\\'):
    "insert all files in the listbox"
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                lb.insert(0, r + "\\" + file)

def open_file():
    os.startfile(lb.get(lb.curselection()[0]))

root = tk.Tk()
root.geometry("400x400")
bt = tk.Button(root, text="Search", command=lambda:searchfiles('.png', 'H:\\'))
bt.pack()
lb = tk.Listbox(root)
lb.pack(fill="both", expand=1)
lb.bind("<Double-Button>", lambda x: open_file())
root.mainloop()
