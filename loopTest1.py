#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is " + str(count))

# this an infinite loop as the wile loop is always running no test on it or break
