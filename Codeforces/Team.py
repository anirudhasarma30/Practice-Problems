#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:56:21 2020

@author: anirudhasarmatumuluri
"""



def solve():
    views = [int(x) for x in input().split()]
    if sum(views)>=2:
        return 1
    return 0

n = int(input())
ans = 0
for i in range(n):
    ans+=solve()
    
print(ans)