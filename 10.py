ms = []
i = 0
num = 0
ms = input('Enter array: ')
for elem in ms[:-1]:
	if ms[i] <= ms[i+1]:
		num += 1
		i += 1
	else:
		print 'False!'
		break
if num == (len(ms)-1):
	print 'True!'
#print ms
#print 'Len(ms) = ', len(ms)
#print 'Num = ', num