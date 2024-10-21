#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:55:33 2024

@author: lidaoyu
"""

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which 
# the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

# s = 'azcbobobegghakl'
# new = ''
# for i in range (len(s)-1):
#     if s[i+1] >= s[i]:
#         print (s[i+1])
#         print (i+1) 
        
   
'''           
s = 'abc1z'
count = ''
lst=[]
for i in range (len(s)-1):
    if s[i-1]<= s[i]:
        if s[i]> s[i+1]:
            count = ''
    count += s[i+1]
    lst.append(count)
print (max(lst, key=len))
 '''   
s = 'zyxwvutsrqponmlkjihgfedcba'
count = s[0]
compare = s[0]
for i in range (len(s)-1):
    if s[i]<= s[i+1]:
        count += s[i+1]
        if len(count) > len (compare):
            compare = count
    else: 
        count = s[i+1]
print('longest substring in alphabetical order is:', compare)
    
#     lst.append(count)
# print (max(lst, key=len and ord))
     
# for i in range (len(s)-3):
#         if s[i-1]<= s[i]:
#         if s[i]<= s[i+1]:
#             if s[i+1]<= s[i+2]:
#                 if s[i+2]<= s[i+3]:
#                     print (s[i-1], s[i], s[i+1], s[i+2], s[i+3]) #beggh
  


  
    
#         count += s[i]
#         num += str(i)
# print (count)
# print (num)  

        
        # print (s[i-1], s[i])
        
        # count += s[i+1]
        
# print (count)
        
        
    
    # if s[i]<= s[i+1] <= s[i+2]:
    #     print (s[i], s[i+1],s[i+2]) #beg egg ggh akl
    # if s[i+1] >= s[i]:
            
        #print (s[i], s[i+1]) #az bo bo be eg gg gh ak kl
        
        
        # new += (''.join((s[i],s[i+1]))) # azbobobeegggghakkl
# print (new)
   




