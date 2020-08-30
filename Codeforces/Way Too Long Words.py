#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:50:14 2020

@author: anirudhasarmatumuluri
"""


def solve():
    ans = input()
    if len(ans)>10:
        ans = ans[0]+str(len(ans)-2)+ans[-1]
    print(ans)


n = int(input())

for i in range(n):
    solve()