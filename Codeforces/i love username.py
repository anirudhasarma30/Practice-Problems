#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:42:55 2020

@author: anirudhasarmatumuluri
"""


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    min = max = arr[0]
    count = 0
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
            count+=1
        if arr[i]<min:
            min = arr[i]
            count+=1
    print(count)


main()