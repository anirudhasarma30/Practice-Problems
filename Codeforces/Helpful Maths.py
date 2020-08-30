#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:05:46 2020

@author: anirudhasarmatumuluri
"""

n1 = 0
n2 = 0
n3 = 0
s = input()
for i in range(0,len(s),2):
    if s[i] == '1':
        n1+=1
    elif s[i] == '2':
        n2 +=1
    else:
        n3+=1
        
ans = "1+" * n1 + "2+" * n2 + "3+" * n3

print(ans[:-1])
    
