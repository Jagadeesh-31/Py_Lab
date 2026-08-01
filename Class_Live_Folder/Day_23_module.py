import Day_23
#(dir(Day_23))

#print(type(Day_23.display()))
'''
print(Day_23.greet("Saketh"))



#print(Day_23.names)

# print(type(Day_23))

Day_23.names.update({'place':'Hyd','age':7})
print(Day_23.names)
'''

# acessing methods  att using from keyword
'''
from Day_23 import greet
print(greet("Agents"))
'''
#print(names)  # error 
'''
from Day_23 import greet,names,display
print(greet("Agents"))
print(names)
print(display)
'''


# to acesss all methods/attributes we use 
# recommand only for userdef/ simple moudles
'''

from Day_23 import *
print(greet("Saketh"))
names.update({'course':'AAI'})
print(names)

y = display()
print(next(y))
print(__name__)
print(__doc__)

print(Day_23.__name__)
print(Day_23.__doc__)
'''

# Bulit-in Modules -->
# math --> 

import math

#print(dir(math))
#print(math.__doc__)

'''
print(math.ceil(2.5))  # it return the higher value

print(math.floor(2.5))  # it return the lower value
print(math.e)
print(math.exp(2))
print(math.factorial(6))
print(math.fmod(5,2))
'''
'''
print(math.log(2))
print(math.log10(2))
print(math.log2(2))

print(math.modf(5.3))
print(math.pi)
print(math.pow(5,3))
print(math.trunc(5.5))
'''


# os ,sys, random,json
'''

import os
#print(dir(os))

#print(os.getcwd()) # return current dir
os.chdir('/home/workspace/my-project/AAI')
print(os.getcwd())
#print(os.listdir())

for i in os.listdir():
    print(i)

#print(os.mkdir('sample')) # make a dir

print(os.removedirs('sample'))

'''

# 
'''
import sys

print(sys.path) # give complete root path 
'''

# random

import random,time

# print(dir(random))

#print(random.random())


# otp generator

for i in range(10):
    print(random.randint(1000,9999))
    time.sleep(5) # sleep 
