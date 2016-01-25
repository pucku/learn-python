# -*- coding: utf-8 -*-
'''
Created on 2016年1月22日

@author: Xin Wan
'''
from Tkinter import *
from tkMessageBox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)
    
top = Tk()
top.title('Echo')

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()