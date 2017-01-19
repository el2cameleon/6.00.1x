#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:59:28 2017

@author: el2cameleon
"""

s = "azcboprrstbobegghaklabcdefghijklmnopqrstuvwxyzdf"
#s = 'zyxwvutsrqponmlkjihgfedcba'
debut = 0
fin =1
s_inter = s[0]
size = 0
max_size = 0
s_end = s_inter

for i in range(len(s)-1):
    if s[debut] <= s[fin]:
        s_inter += s[fin]
        #print(str(i) + " " + str(debut) + " " + str(fin) + " " + s_inter + " " + str(size))
        size = len(s_inter)
        if size > max_size:
            max_size = size
            s_end = s_inter
            #print(str(i) + " " + str(debut) + " " + str(fin) + " " + s_inter + " " + str(size))
        debut += 1
        fin += 1
        #print(str(i) + " " + str(debut) + " " + str(fin) + " " + s_inter + " " + str(size))
    else:
        s_inter = s[fin]
        size = len(s_inter)
        #print(str(i) + " " + str(debut) + " " + str(fin) + " " + s_inter + " " + str(size))

        debut += 1
        fin += 1
        #print(str(i) + " " + str(debut) + " " + str(fin) + " " + s_inter + " " + str(size))
print("Longest substring in alphabetical order is: " + s_end)

