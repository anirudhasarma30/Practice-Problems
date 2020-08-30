#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:40:46 2020

@author: anirudhasarmatumuluri
"""
def isPrime(n):
    if n == 1:
        return True
    
    for i in range(2,int(pow(n,(1/2)))+1):
        if n%i == 0:
            return False
    return True
    
def main():
    n,m = [int(x) for x in input().split()]
    if not isPrime(m):
        print("NO")
        return
    else:
        for i in range(n+1, m):
            if isPrime(i):
                print("NO")
                return
    print("YES")
    return

main()
