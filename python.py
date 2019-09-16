# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:11:13 2019

@author: user
"""
import pandas as pd
import numpy as np
arr=np.array([1,2,3,4,7])
print(arr)
s=pd.Series()
print(s)
list1=['a',12,13]
tuple1=(1,1,34,4,'e')
print(tuple1)
s4=pd.Series(list1)
print(s4)
s5=pd.Series(list1,index=['nescafe','brookbond','taj'])
print(s5)
s6=pd.Series(arr,index=['m','s','p','t','y'])
print(s6)
dict={'nescafe':11,'brookbonde':12,'taj':13}
s3=pd.Series(dict,index=['a','b','c'])
print(s3)
print(s6[2:5])
print(s6[2:-1])


df1=pd.DataFrame()
print(df1)
list2=['a','b','c']
df1=pd.DataFrame(list2)
print(df1)
list3=[1,2,4]
df1=pd.DataFrame(list1,list3,list2)
print(df1)