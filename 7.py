card = raw_input('Please Enter Number of the Debit Card:\n')
if len(card) == 16:
	card2 = card[-1:-5:-1]
	print card[0:4] + '********' + card2[::-1]
else:
	print "Sike! That's the Wrong Number!"