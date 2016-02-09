N = input("Write your age please: ")
if N == 1 or N == 21 or N == 31 or N == 41 or N == 51 or N == 61 or \
     N == 71 or N == 81 or N == 91:
    print N, 'god'
elif N in xrange(2, 5) or N in xrange(22, 25) or N in xrange(32, 35) \
       or N in xrange(42, 45) or N in xrange(52, 55) or N in xrange \
       (62, 65) or N in xrange(72, 75) or N in xrange(82, 85) or N in \
       xrange(92, 95):
    print N, 'goda'
elif N in xrange(5, 21) or N in xrange(25, 31) or N in xrange(35, 41) \
       or N in xrange(45, 51) or N in xrange(55, 61) or N in xrange \
       (65, 71) or N in xrange(75, 81) or N in xrange(85, 91) or \
       N in xrange(95, 101):
    print N, 'let'
else:
    print 'Nope'