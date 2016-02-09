dot = '.'
mon = raw_input('\nEnter the Amount of Money! \n(format: xxx.xx)\n')

#searching for the character '.' on the cut mstr

md = mon.find(dot)
print md

if float(mon) > 0 and md == -1:
	print mon + ' rubles ' + ' 00 kopeks'
	quit()

#searching for the value of rubles

rub = mon[:md]
print rub

#searching for the value of kopeks

kop = mon[md+1:]
print kop

try:
    if float(mon) < 0 or len(kop) >= 3:
    	raise ValueError
except ValueError:
    print'\nInvalid Money Value! Please Enter Correct Value!'
    quit()

if len(kop) == 2:
	print rub + ' rubles ' + kop + ' kopeks'
elif len(kop) == 1:
	print rub + ' rubles ' + kop + '0 kopeks'
