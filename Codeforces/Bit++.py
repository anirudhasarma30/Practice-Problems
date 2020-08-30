#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:52:39 2020

@author: anirudhasarmatumuluri
"""

n = int(input())
x = 0
while n>0:
    line = input()
    if line[1] == "+": x+=1
    else: x-=1
    n-=1
print(x)