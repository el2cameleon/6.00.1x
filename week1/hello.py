#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:18:11 2017

@author: el2cameleon
"""

#i = 0
#j = 0
#for i in range(5):
#    j += 2
#    print(j)
#print("Goodbye!")

#print("Hello!")
#i = 0
#j = 10
#for i in range(5):
#    print(j)
#    j -= 2
 
#end = 17

#j = 0
#for i in range(end):
#    j = j + i + 1
#print(j)
#for letter in 'hola':
#    print(letter)
    
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
    
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)