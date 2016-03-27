# -*- coding: utf-8 -*-

arr = []
while True:
    try:
        N = int(input('\nEnter the Number: '))
        if N > 0:
            break
        else:
            print ("\nSike! That's the Wrong Number!")
    except ValueError:
        print ("Wrong Number")
        
for x in range(1,99):
    for y in range(1,99):
        for z in range(1,99):
            if x**3 + y**3 + z**3 == N:
                arr = [x, y, z]
                print ([x, y, z])
if arr == []:
    print ("\nNot such combinations!")