# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
from initdata import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile, None)
    recfile.close()