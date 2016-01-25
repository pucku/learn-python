# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
import shelve
db = shelve.open('people-shelve')
for key in db:
    print key, '=>', db[key]
print db['sue']['name']
db.close()