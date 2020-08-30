#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:48:45 2020

@author: anirudhasarmatumuluri
"""



def main():
    num1 = input()
    num2 = input()
    for x in zip(num1, num2):
        a,b = tuple(x)
        if a == b:
            print('0',end = "")
        else:
            print('1',end = "")
    return

main()