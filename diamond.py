# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:11:25 2019

@author: user
"""

for i in range(4):
    print(i,end=" ")
    for j in range(i):
        print("* ")
        
a=[1,2,3,4,5]
s=7
for i in range(len(a)):
    for j in range(i):
        if(s==a[i]+a[j]):
            print("elements present at index",i,j)

s1='abcdefgh'
s2='def'
for i in range(len(s1)):
    print(i)
    for j in range(len(s2)):
        print(j)
        if(s2[j]==s1[i]):
            u=len(s2)
            while u<=0:
                s2[u]=s2[j]
                u-=1
print(reverse(s2) )
print(s2)
                
            
import random
arr=[]
for x in range(10):
   
    arr.append(random.randint(1,100))
print(arr)