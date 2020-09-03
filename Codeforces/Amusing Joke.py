#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:44:05 2020

@author: anirudhasarmatumuluri
"""

host = input()
guest = input()
pile = input()

arr = [0]*26

for letter in guest:
    arr[ord(letter)-ord('A')]+=1
    
for letter in host:
    arr[ord(letter)-ord('A')]+=1
    
for letter in pile:
    arr[ord(letter)-ord('A')]-=1
    
flag = False
    
for x in arr:
    if x!=0:
        flag = True
        print("NO")
        break
if flag==False:
    print("YES")
        