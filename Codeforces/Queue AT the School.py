#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:53:35 2020

@author: anirudhasarmatumuluri
"""

def main():
    n,t = [int(x) for x in input().split()]
    word = input()
    arr = [letter for letter in word]
    #print(arr)
    for i in range(t):
        j = 0
        while j<(n-1):
            #print("outside check j = ",j)
            if (arr[j]=='B')&(arr[j+1]=='G'):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                j+=1
                #print("inside check j = ",j)
            j+=1
    print("".join(arr))
    return

    
    
    
main()