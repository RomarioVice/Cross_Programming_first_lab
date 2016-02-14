for N in xrange(1,100001):
    print '\nValue', N, 'have next combinations:\n'
    for x in xrange(1,48):
        for y in xrange(1,48):
            for z in xrange(1,48):
                if x ** 3 + y ** 3 + z ** 3 == N:
                    if (x == y and x == z and y == z):
                        continue
                    else:
                        print [x, y, z]