# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:42:25 2016

@author: Roma
"""

import os, hashlib

dir = "D:\DNU\CrossProgramming\Cross_Programming_first_lab"

for root, dirs, files, in os.walk(dir):
    for name in files:
        fullname = os.path.join(dir, name)
        if os.path.isfile(fullname):
            checksum = hashlib.md5().hexdigest()
            print(checksum)