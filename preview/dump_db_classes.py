# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
import shelve
db = shelve.open('class-shelve')
for key in db:
    print key, '=>', db[key].name, db[key].pay
    
bob = db['bob']
print bob.lastName()
print db['tom'].lastName()