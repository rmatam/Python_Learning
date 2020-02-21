# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:59:31 2020

@author: Rajasekhar.Matam
"""

class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
        
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myfunc(mysillyobject):
        print("this is the first function from "+ mysillyobject.name)
        
p1 = Person("john",32)        
print(p1.age)
print(p1.name)
p1.myfunc()

class Person2:
    pass

    