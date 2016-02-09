st = raw_input('Please Enter URL: ')
w3 = 'www'
dc = 'moc.'
if st[0:3] == w3:
	st = 'http://' + st
	if (st[-1:-5:-1]) != dc:
		st = st + '.com' 
print st