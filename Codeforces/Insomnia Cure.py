#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:23:49 2020

@author: anirudhasarmatumuluri
"""
def primeSet(arr):
    ans = set()
    for x in arr:
        while x%2==0:
            ans.add(2)
            x = x//2
        
        for i in range(3, int(pow(x,(1/2)))):
            while x%i==0:
                x = x//i
                ans.add(i)
        if x>2:
            ans.add(x)
    return list(ans)


def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    if (k==1)or(l==1)or(m==1)or(n==1):
        return d
        
    else:
        primes = primeSet([k,l,m,n])
        size = len(primes)
        
        if size == 1:
            return d//primes[0]
        
        
        ans = 0
        ans+= (d//primes[0])
        ans+=(d//primes[1])
        ans-=(d//(primes[0]*primes[1]))
        if size == 2:
            return ans
        
        ans+=(d//primes[2])
        ans-=(d//(primes[1]*primes[2]))
        ans-=(d//(primes[0]*primes[2]))
        ans+=(d//(primes[0]*primes[1]*primes[2]))
        if size == 3:
            return ans
        
        ans+=(d//primes[3])
        ans-=(d//(primes[0]*primes[3]))
        ans-=(d//(primes[1]*primes[3]))
        ans-=(d//(primes[2]*primes[3]))
        
        ans+=(d//(primes[1]*primes[2]*primes[3]))
        ans+=(d//(primes[0]*primes[2]*primes[3]))
        ans+=(d//(primes[0]*primes[2]*primes[3]))
        
        ans-=(d//(primes[0]*primes[1]*primes[2]*primes[3]))
        
        if size == 4:
            return ans
            
            
        
        
    

print(main())