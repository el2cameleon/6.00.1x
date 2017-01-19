#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

countVowels = 0
s = str(input("Enter a phrase: "))

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        countVowels += 1
print("Number of vowels: " + str(countVowels))
