# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 00:40:08 2020

@author: Rajasekhar.Matam
"""

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

import numpy
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()

x = numpy.random.normal(1,1,1000)
y = numpy.random.normal(1,2,1000)
plt.scatter(x,y)

plt.hist(x,bins = 500)

z = numpy.percentile(x,25)
print(z)

sd = numpy.std(x)
print(sd)

varien = numpy.var(x)
print(varien)

mean = numpy.mean(x)
print(mean)
