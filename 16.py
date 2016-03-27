# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:09:51 2016

@author: Roma
"""

import re, collections

f = open('text.txt', 'rt')

arr = []
for line in f:
    arr += re.findall(r'[A-Za-z]', line)
arr = ''.join(arr)
arr = arr.upper()
print (collections.Counter(arr).most_common())

f.close()