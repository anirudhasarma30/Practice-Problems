#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:00:46 2020

@author: anirudhasarmatumuluri
"""


def main():
    n = int(input())
    c = 0
    m = 0
    for i in range(n):
        a,b = [int((x)) for x in input().split()]
        c-=a
        c+=b
        m = max(m,c)
        
    print(m)
    return
main()