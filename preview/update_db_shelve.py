# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.5
db['sue'] = sue 
db['tom'] = tom
db.close()