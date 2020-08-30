#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:20:27 2020

@author: anirudhasarmatumuluri
"""

def main():
    word = input()
    word = word[::-1]
    s = [letter for letter in word]
    while len(s)!=0:
        ans = s.pop()
        if ans == ".":
            print("0",end = "")
        elif ans == "-":
            ans+=s.pop()
            if ans == "-.":
                print("1", end = "")
            elif ans == "--":
                print("2", end = "")
    return


main()