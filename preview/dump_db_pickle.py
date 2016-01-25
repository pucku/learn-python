# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print key, '=>', db[key]
    
print(db['sue']['name'])