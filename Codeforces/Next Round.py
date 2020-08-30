#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:15:48 2020

@author: anirudhasarmatumuluri
"""

n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
ans = 0
for x in arr:
    if (x>=arr[k-1]) & (x>0):
        ans+=1
print(ans)

