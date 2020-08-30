#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:22:34 2020

@author: anirudhasarmatumuluri
"""

n = int(input())
s = input()
ans = 0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        ans+=1
print(ans)
    