#libs
import tkinter
import sqlite3
import pathlib
import os
#DEF
def windows():
    #windows
    global mwindows
    mwindows = tkinter.Tk()
    mwindows.title('main')
    mwindows.geometry('800x600')
    database = sqlite3.connect('database.db')
    c = database.cursor()
    menu()
    mwindows.mainloop()
def menu():
    menu = tkinter.Menu(mwindows)
    mwindows.config(menu= menu)
    test = tkinter.Menu(menu, tearoff=0)
    menu.add_cascade(label='test', menu= test)
    test.add_command(label='test1')
#load database
path = pathlib.Path('./database.db')
if os.path.isfile(path):
    print('hola')
    windows()
else:
    windows()