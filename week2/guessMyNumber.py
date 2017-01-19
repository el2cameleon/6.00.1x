#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:43:00 2017

@author: el2cameleon
"""


low = 0
high = 100
guess = int((high)/2)
test = 'a'
print("Please think of a number between 0 and 100!")
print("Is your secret number  " + str(guess) + "?")
while test != 'c':
 while test != 'l' and test != 'h':
     test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
     if test == 'l':
         low = guess
         guess = int((high + low)/2)
         print("Is your secret number is: " + str(guess))
         test = 'a'
     elif test == 'h':
         high = guess
         guess = int((high + low)/2)
         print("Is your secret number is: " + str(guess))
         test ='a'
     elif test == 'c':
         break
     else:
         print("Sorry, I did not understand your input.")
         print("Is your secret number  " + str(guess) + "?")



print("Game over. Your secret number was: " + str(guess))
