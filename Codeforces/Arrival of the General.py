#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:09:15 2020

@author: anirudhasarmatumuluri
"""

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    max = arr[0]
    min = arr[0]
    minindex = 0
    maxindex = 0
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
            maxindex = i
        if arr[i]<=min:
            min = arr[i]
            minindex = i
            
    
    time = maxindex-1
    if maxindex>minindex:
        time-=1
    
    time+=(n-minindex)
    print(time)
    
    
    
    
    
main()