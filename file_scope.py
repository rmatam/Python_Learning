# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:55:22 2020

@author: Rajasekhar.Matam
"""

def myfun():
    x = 200
    print(x)
    
myfun()

def myfun():
    x = 200
    print(x)
    def myinnerfunct():
        print(x)
    myinnerfunct()

myfun()


x = 400

def myfunc():
    x = 350
    print(x)
myfunc()
print(x)

x =450
def myfunc():
    global x
    x = 250
    print(x)
    
myfunc()

print(x)
