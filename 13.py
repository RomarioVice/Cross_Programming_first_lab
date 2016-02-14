st = raw_input('Enter String:\n')
stm = st.split()
st = ''
elem = 1
for i in stm:
	if i[-1] == '.':
		st += i[0:-1] + '(' + str(elem) + ')' + '. '
		elem += 1
	elif i[-1] == ',':
		st += i[0:-1] + '(' + str(elem) + ')' + ', '
		elem += 1
	elif i[-1] == '!':
		st += i[0:-1] + '(' + str(elem) + ')' + '! '
		elem += 1
	elif i[-1] == '?':
		st += i[0:-1] + '(' + str(elem) + ')' + '?'
		elem += 1
	elif i[-1] == '/':
		st += i[0:-1] + '(' + str(elem) + ')' + '/'
		elem += 1
	elif i == '-':
		st += '- '
	else:
		st += i + '(' + str(elem) + ')' + ' '
		elem += 1
print '\nResult:'
print st