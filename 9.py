import random, math

#N = 70
#N = 256
#N = 512

N = random.randint(1, 1000)
SP = [random.randint(1,9999) for i in range(N)]
ST1 = math.log(N,2)
if 2 ** ST1 == N: 
    ST2 = int(ST1)
else: 
    ST2 = int(ST1 + 1)
SP2 = int((2 ** ST2) - N)
SP = SP + [0] * SP2

#printing some information 

print '\nCreated Array:\n', '\n', SP
print '\nSome Information:'
print '\nThe Amount of Numbers: ', N
print '\nFirst Extent of 2:', ST1
print '\nThe Nearest Extent of 2:', ST2
print '\nThe Amount of Numbers in the Nearest Extent of 2:', N + SP2
print '\nThe Number of Zeros:', SP2