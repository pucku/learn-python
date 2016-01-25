# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
from initdata import db
import pickle
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()