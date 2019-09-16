# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:12:07 2019

@author: user
"""

def inner(**args):
    
    for key,value in args.items():
        #printString="{:20}{:10}".format()
        print("{} is {}".format(key,value))
            
inner(name='kriti',age='21',phone='458484')

True=False
print(True)
while True:
    print(True)
    break