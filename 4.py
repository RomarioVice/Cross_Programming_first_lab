num = input('\nEnter the number of terms: ')
if num == 1:
	print 'Result = 1'
elif num == 0:
	print 'Result = 0'
else: 
    i = 1.00
    j = 1
    pi1 = 1.00/i
    pi2 = 1.00
    while j < num: 
        i += 2.00
        #print i
        pi2 = (1/i)
        if j % 2 != 0:
    	    pi2 *= -1
        #print pi2
        pi = pi1 + pi2
        pi1 = pi
        #step
        j = j + 1
        #print pi
    print 'Result =', pi