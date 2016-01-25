# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
        
if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print bob.name, sue.pay
    
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
    
    people = [bob, sue]
    for person in people:
        print person.name, person.pay
        
    x = [(person.name, person.pay) for person in people]
    print x
    
    print [rec.name for rec in people if rec.age >= 45]
    
    print [(rec.age **2 if rec.age >= 45 else rec.age) for rec in people]