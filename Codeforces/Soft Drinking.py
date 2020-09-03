#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:50:39 2020

@author: anirudhasarmatumuluri
"""

n, k, l, c, d, p, nl, np = [int(x) for x in input().split()]
ans = min((k*l)//nl, p//np)
ans = min(ans,(c*d)//n)
ans = min(ans,n)
print(ans)