num = xrange(10,100)
j = 1
print num
for i in num:
    dec = float(i // 10)
    un = float(i % 10) 
    if  (dec + un) % 7 == 0:
    	print '\nNumber', j, '=', i
    	j += 1
    else:
    	continue