# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:00:16 2016

@author: Roma
"""

while True:
    try:
        strn = input("Enter the String: ")
        if len(strn) > 0:
            break
        else:
            print("String is Empty. Enter the String.")
    except ValueError:
        print ("Empty String")
        
        
fl = True   
for i in range(len(strn)-1):
    for j in range(len(strn)):
        if strn[i]==strn[j] and i!=j: 
            fl = False
            break
    if fl == True and i!=' ':
        print (strn[i])
    fl = True
print(strn[-1])