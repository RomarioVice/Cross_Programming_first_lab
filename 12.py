# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:11:46 2016

@author: Roma
"""

for N in range(1,100000):
    arr1=[]
    arr2=[]
    x = 0
    y = 0
    z = 0
    step = 0
    st = int(N**(1/3.0)+2)
    for z in range(0,st):
        for y in range(z,st):
            for x in range(y,st):
                if x**3+y**3+z**3==N:
                    arr1 = [x, y, z]
                    arr2 += list(map(lambda i: arr1[3*i:(i+1)*3], range(1)))
                    step += 1
    if(step >= 3):
        print (N, arr2)