#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:52:51 2024

@author: lidaoyu
"""

#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s = 'azcbobobegghakl'
vowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'i'\
    or char == 'o' or char == 'u':
        vowels += 1

print ('Number of vowels: ', vowels)


    