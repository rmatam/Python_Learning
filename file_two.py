# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:16:14 2020

@author: Rajasekhar.Matam
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
x = Person("john","max")        
x.printname()

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
    #pass

x = Student("sarad","dinda1")
x.printname()

class student1(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduuation = year
        
    def welcome(self):
        print("Welcome", self.firstname,self.lastname,"to the class of" ,self.graduuation)
        
        
x = student1("raja","sekhar", 2019)
x.printname()
x.graduuation

x.welcome()
