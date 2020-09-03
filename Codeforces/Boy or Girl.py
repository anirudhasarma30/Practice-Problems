#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:41:37 2020

@author: anirudhasarmatumuluri
"""

string = input()
if len(set(string))%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")