# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 03:03:55 2019

@author: user
"""
num = int(input("enter the value of rows"))
for i in range(0,num):
    for i in range(0,num-i-1):
        print(" ")
    print("*")