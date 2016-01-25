# -*- coding: utf-8 -*-
'''
Created on 2016年1月22日

@author: Xin Wan
'''
from Tkinter import *
from tkinter102 import  MyGui

#main app window 
mainwin = Tk()
Label(mainwin, text=__name__).pack()

#popup window 
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()