# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:26:56 2020

@author: Rajasekhar.Matam
"""

import json


x = '{"name":"raj","age":36}'
print(x)

y = json.loads(x)
print(y)

print(y["age"])
y["age"]


x = {"Name":"raja", "age":34}

y = json.dumps(x)
print(y)

import re

x = re.split(" ", "my name is raj ")
print(x)

for y in x:
    print(y)
    
txt = "the rain in spain and italy"
x = re.sub("\s", "9",txt,4 )
print(x)
