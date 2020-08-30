#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:30:52 2020

@author: anirudhasarmatumuluri
"""
def isDistinct(year):
    digits = set([letter for letter in year])
    if len(digits)!=4:
        return False
    return True
    


def main():
    y = int(input())
    y+=1
    while not isDistinct(str(y)):
        y+=1
    
    print(y)
    
    
    
    return

main()