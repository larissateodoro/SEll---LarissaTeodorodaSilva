#Modulo de importação
"""from my_module import find_index, test 
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
#print(Test)

print(sys.path)"""

#Bibliotecas
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_courses = random.choice(courses)

print(random_courses)

import math

courses = ['History', 'Math', 'Physics', 'CompSci']

rads = math.radians(90)

print(math.sin(rads))

import datetime
import calendar 

courses = ['History', 'Math', 'Physics', 'CompSci']

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os

courses = ['History', 'Math', 'Physics', 'CompSci']

print(os.__file__)

import antigravity