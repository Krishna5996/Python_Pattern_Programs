# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:11:04 2019

@author: user
"""
s='krishna'
s1="krish"
def reverse(s):
    if len(s)== 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
print(reverse(s))    

a=''
b=''
s[0]="q"
print(s)
for i in range(len(s1)):
    for j in range(i):
        if s[i]==s1[i]:
            s[::1],s[:i+1]=s[i+1],s[i] 
print(s)
'''
for j in range(len(s1)):
    if s[j]!=s1[j]:        
        b+=s[i]  
print(reverse(a))
print(b)
'''
 