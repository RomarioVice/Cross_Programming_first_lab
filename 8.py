st = raw_input('Please Enter the Sting: ')

#removing punctuation marks------------------------------

for i in st:
    if i == '.':
        st = st.replace('.','')
    elif i == ',':
        st = st.replace(',','')
    elif i == '!':
        st = st.replace('!','')
    elif i == '?':    		
    	st = st.replace('?','')

#--------------------------------------------------------

sp = st.split()
#print st
sp7 = []
sp47 = []
sp4 = []
for w in sp:
	if len(w) > 7:
		sp7.append(w)
	elif len(w) > 4 and len(w) < 7: 
		sp47.append(w)
	else:
		sp4.append(w)

#printing lists of words---------------------------------

print '\nMore then 7 characters: ',sp7
print '\nMore then 4 but less then 7 characters:',sp47
print '\nLess then 4 or equal:',sp4