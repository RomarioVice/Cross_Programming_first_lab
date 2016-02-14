while True:
    try:
        N = input("Vvedite 4islo: ")       
        if (N>0):
            break
    except:
        print "Error value"
m=[]
for x in range(48):
    for y in range(48):
        for z in range(48):
            if x**3+y**3+z**3==N:
                m = [x, y, z]
if m==[]:
    print 'Nothing to find'
else:
    print m