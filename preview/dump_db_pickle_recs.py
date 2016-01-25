# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
import pickle, glob 
for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print filename, '=>', record 

suefile = open('sue.pkl', 'rb')
print pickle.load(suefile)['name']