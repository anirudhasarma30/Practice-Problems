#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:18:36 2020

@author: anirudhasarmatumuluri
"""

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(sum(arr)/n)
    
    
main()