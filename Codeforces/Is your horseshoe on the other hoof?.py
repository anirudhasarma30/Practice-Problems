#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:39:47 2020

@author: anirudhasarmatumuluri
"""

s1,s2,s3,s4 = [int(x) for x in input().split()]

print(4-len(set([s1,s2,s3,s4])))