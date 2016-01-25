# -*- coding: utf-8 -*-
'''
Created on 2016年1月20日

@author: Administrator
'''
dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print >> dbfile, str(key)
        for (name, value) in db[key].items():
            print >> dbfile, str(name) + RECSEP + repr(value)
        print >> dbfile, ENDREC
    print >> dbfile, ENDDB
    
    dbfile.close()
    
def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db    
        
    
if __name__ == '__main__':
    from initdata import db
    storeDbase(db, dbfilename)