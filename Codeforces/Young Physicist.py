#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:43:41 2020

@author: anirudhasarmatumuluri
"""

def main():
    n = int(input())
    x =0
    y = 0
    z = 0
    for i in range(n):
        i,j,k = [int(x) for x in input().split()]
        x+=i
        y+=j
        z+=k
        
    if (x==0)&(y==0)&(z==0):
        print("YES")
    else:
        print("NO")
    return

main()