#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:01:00 2020

@author: anirudhasarmatumuluri
"""

arr = []
x = None
y = None
for i in range(5):
    arr.append([x for x in input().split()])
    if "1" in arr[i]:
        x = i
        y = arr[i].index("1")
        
print(abs(int(x)-2)+abs(int(y)-2))