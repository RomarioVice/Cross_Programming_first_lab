# -*- coding: utf-8 -*-

N = 0
while True:
     try:
            N = int(input("Enter Your Age: "))
            if N>0 and N<=100:
                break
            else:
                print ("Age must be on range from 1 to 100!")
     except ValueError:
            print ("Wrong Number")


if (N == 1 or 
    N == 21 or 
    N == 31 or 
    N == 41 or 
    N == 51 or 
    N == 61 or
    N == 71 or 
    N == 81 or 
    N == 91):
    print (N, 'god')
    
elif (N in range(2, 5) or 
    N in range(22, 25) or 
    N in range(32, 35) or 
    N in range(42, 45) or 
    N in range(52, 55) or 
    N in range(62, 65) or 
    N in range(72, 75) or 
    N in range(82, 85) or 
    N in range(92, 95)):
    print (N, 'goda')

elif (N in range(5, 21) or 
    N in range(25, 31) or 
    N in range(35, 41) or 
    N in range(45, 51) or 
    N in range(55, 61) or 
    N in range(65, 71) or 
    N in range(75, 81) or 
    N in range(85, 91) or
    N in range(95, 101)):
    print (N, 'let')