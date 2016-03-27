# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:34:12 2016

@author: Roma

"""

while True:
    try:
        strn = input('Enter the String Here: ')
        if len(strn) > 0:
            break
        else:
            print ('String is Empty. Enter the String Please: ')
    except ValueError:
        print ('Empty String')
        
copystrn = ''
index = 0
arr = strn.split(' ')
for num in arr:
    if num.strip() != '-' and len(num.strip())>0:
        copystrn += num + '(' + str(index) + ') '
    else:
        copystrn += num
    index += 1
    
print ('/n', copystrn)