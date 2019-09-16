# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:52:04 2019

@author: user
"""

def main():
    k=sum(10)
    print("sum: ",k)
def sum(a):
    if(a==1):
        return a
    s=a+sum(a-1)
    return s
main()

import os
os.getcwd()