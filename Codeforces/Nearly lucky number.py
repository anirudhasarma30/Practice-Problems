#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:11:02 2020

@author: anirudhasarmatumuluri
"""

def isLucky(num):
    s = set([x for x in num])
    if len(s)>2:
        return False
    if ('4' in s)& ('7' in s):
        return True
    if (('4' in s)or('7' in s))&(len(s)==1):
        return True
        
        
    
    
    return False

def main():
    num = input()
    count = 0
    for digit in num:
        if (digit == '4') or (digit=='7'):
            count+=1
    if isLucky(str(count)):
        print("YES")
    else:
        print("NO")
    return

main()