# -*- coding: utf-8 -*-
'''
Created on 2016年1月22日

@author: Administrator
'''
from Tkinter import mainloop
from tkMessageBox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()