# -*- coding: utf-8 -*-
'''
Created on 2016年1月22日

@author: Xin Wan
'''
from Tkinter import *
from tkMessageBox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()