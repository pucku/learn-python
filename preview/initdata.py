# -*- coding: utf-8 -*-
'''
Created on 2016年1月20日

@author: Xin Wan
'''
#initialize data to be stored in files, pickles, shelves

#records 
bob = {'name':'Bob Smith', 'age':42, 'pay': 30000, 'job':'dev'}
sue = {'name':'Sue Smith', 'age':42, 'pay': 30000, 'job':'dev'}
tom = {'name':'Tom', 'age':3, 'pay': 30000, 'job':'dev'}

#database 
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print key, '=>', db[key]