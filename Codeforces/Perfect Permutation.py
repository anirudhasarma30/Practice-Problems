#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:02:32 2020

@author: anirudhasarmatumuluri
"""



def main():
    n = int(input())
    if (n%2)!=0:
        print(-1)
    else:
        for i in range(0,n,2):
            print(i+2,i+1,end = " ")
    
main()