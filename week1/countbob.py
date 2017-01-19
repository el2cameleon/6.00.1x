#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:17:01 2017

@author: el2cameleon
"""

sInter = ""
debut = 0
fin = 3
countbob = 0
s = "azcbobobebggdabobzertyuiopbobbzert"
for i in range(len(s)):
    sInter = s[debut:fin]
    print(str(debut) + " " + str(fin) + " " + sInter)
    debut += 1
    fin += 1
    if sInter == "bob":
        countbob += 1
        sInter = ""
    else:
        sInter = ""
print("Number of times bon occurs is :" + str(countbob))

