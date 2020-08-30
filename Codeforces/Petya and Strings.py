#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:56:26 2020

@author: anirudhasarmatumuluri
"""

str1 = input().lower()
str2 = input().lower()

if str1==str2:
    print(0)
elif str1>str2:
    print(1)
else:
    print(-1)
