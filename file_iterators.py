# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:33:04 2020

@author: Rajasekhar.Matam
"""

mytuple = ("raj","sekhar","dattu")
mytuple
myit = iter(mytuple)
for x in mytuple:
    print(x)

print(next(myit))

mystr = "xxxx"
myit = iter(mystr)
next(myit)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
            
    
myclass = MyNumbers()
myiter = iter(myclass)    
next(myiter)

for x in myiter:
    print(x)
