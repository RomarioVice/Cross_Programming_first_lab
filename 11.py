arr = []
N = input('\nEnter the Number: ')
if N <= 0:
    print "\nSike! That's the Wrong Number!"
else:
    for x in xrange(1,99):
        for y in xrange(1,99):
            for z in xrange(1,99):
                if x**3 + y**3 + z**3 == N:
                    arr = [x, y, z]
                    print [x, y, z]
    if arr == []:
        print "\nDoes't have values!!!"