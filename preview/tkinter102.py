# -*- coding: utf-8 -*-
'''
Created on 2016年1月22日

@author: Xin Wan
'''
from Tkinter import *
from tkMessageBox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()
        
    def reply(self):
        showinfo(title='popup', message='Button pressed!')
        
if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()