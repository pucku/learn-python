# -*- coding: utf-8 -*-
'''
Created on 2016年1月21日

@author: Xin Wan
'''
from person import Person
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
        
    def giveRaise(self, percent, bonus = 0.1):
        self.pay *= (1.0 + percent + bonus)
#         Person.giveRaise(self, percent + bonus)
        
if __name__ == '__main__':
    tom = Manager('Tom Doe' , age = 50 , pay = 50000)
    print tom.lastName()
    tom.giveRaise(.20)
    print tom.pay
    
    print tom