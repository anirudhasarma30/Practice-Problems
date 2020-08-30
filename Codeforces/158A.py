#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:01:46 2020

@author: anirudhasarmatumuluri
"""

n,k = input().split()
k = int(k)
n = int(n)

arr = [int(x) for x in input().split()]
print("k = "+str(k))
print(arr)
kth = arr[k]
print(len([x for x in arr if x>=kth]))