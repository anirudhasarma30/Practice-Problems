#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:01:37 2020

@author: anirudhasarmatumuluri
"""
def main():
    word = input()
    lower = 0
    upper = 0
    
    for letter in word:
        if letter == letter.lower():
            lower+=1
        else:
            upper+=1
    if lower>=upper:
        print(word.lower())
    else:
        print(word.upper())



main()