#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:04:44 2020

@author: anirudhasarmatumuluri
"""

def main():
    n = int(input())
    doors = []
    for i in range(n):
        l,r = [int(x) for x in input().split()]
        doors.append((l,r))
    lopen = 0
    ropen = 0
    for door in doors:
        lopen+=door[0]
        ropen+=door[1]

    
    ans = 0
    if lopen>(n//2):
        ans+=(n-lopen)
    else:
        ans+=lopen
        
    if ropen>(n//2):
        ans+=(n-ropen)
    else:
        ans+=ropen
    
    
    print(ans)
    return


main()

