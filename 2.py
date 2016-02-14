print '\nEnter date please!' 

#DAY-------------------------------------------------------------------

d = raw_input("\nEnter the Day! (format: dd): ")

#searching for character '0' on the string d 

ds1 = d.find('0',0,1)
ds2 = d.find('0',1)

#exception if negative value of the day

try:
    if int(d) < 0:
	    raise ValueError
except ValueError:
    print '\nNegative Value of the Day! Please Enter Correct Value!!!' 
    quit()  

#print ds1
#print ds2

if ds1 == -1 and ds2 == -1 and len(d) == 1:
    d = '0' + d
else:
    d = d

#MONTH-----------------------------------------------------------------

m = raw_input('\nEnter the Month! (format: mm): ')

#searching for character '0' on the string m

ms1 = m.find('0',0,1)
ms2 = m.find('0',1)

#exception if negative value of the month

try:
    if int(m) < 0:
	    raise ValueError
except ValueError:
    print '\nNegative Value of the Month! Please Enter Correct Value!!!'
    quit()

#print ms1
#print ms2	
if ms1 == -1 and ms2 == -1 and len(m) == 1:
    m = '0' + m
else:
    m = m

#YEAR------------------------------------------------------------------

y = raw_input('\nEnter the Year! (format: yyyy): ')	

#exception if negative value of the year

try:
    if int(y) < 0:
	    raise ValueError
except ValueError:
    print '\nNegative Value of the Year! Please Enter Correct Value!!!'
    quit()

#print result

print d,'/', m, '/', y