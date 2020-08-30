#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:38:08 2020

@author: anirudhasarmatumuluri
"""
def isValid(x,y):
    if (x>=0)&(y>=0)&(x<3)&(y<3):
        return True
    return False

def main():
    lights = []
    for x in range(3):
        lights.append([0,0,0])
    flicks = []
    for i in range(3):
        flicks.append([int(x) for x in input().split()])
    
    for i in range(3):
        for j in range(3):
            if flicks[i][j]!=0:
                #print(lights)
                #print("INITIATED")
                lights[i][j]+=flicks[i][j]
                #print()
                #print("initials lights")
                #print(lights)
                if isValid(i,j-1):
                    lights[i][j-1]+=flicks[i][j]
                    #print(lights)
                    #print("GOT HERE1")
                
                if isValid(i,j+1):
                    lights[i][j+1]+=flicks[i][j]
                    #print(lights)
                    #print("GOT HERE2")
                
                if isValid(i-1,j):
                    
                    lights[i-1][j]+=flicks[i][j]
                    
                    #print("GOT HERE3")
                    
                if isValid(i+1,j):
                    
                    lights[i+1][j]+=flicks[i][j]
                    #print(lights)
                    #print("GOT HERE4")
        #break        
    for i in range(3):
        for j in range(3):
            if lights[i][j]%2!=0:
                print(0,end = "")
            else:
                print(1, end = "")
        print()
        
        
        
        
        
main()
'''
for i in range(3):
    for j in range(3):
        print("For ",i,",",j,":")
        arr = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for x in arr:
            print("(",x[0],",",x[1],") is ", isValid(x[0],x[1]))
    print()'''