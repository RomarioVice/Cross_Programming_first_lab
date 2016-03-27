# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:38:00 2016

@author: Roma
"""

import re
strin = input('Enter the String Here: ')
strin = re.findall(r'(\b[A-Z][a-z]+\d{2,2})\b', strin)
print ('Result: ', strin)