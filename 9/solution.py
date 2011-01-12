def isPyt(a, b, c):
    return a*a + b*b == c*c

for m in xrange(1,100):
    for n in xrange(1, 100):
        a = 2*n*m
        b = m*m - n*n
        c = m*m + n*n
        if isPyt(a,b,c):
            #print "Pyt: %d,%d,%d" % (a,b,c)
            if a+b+c == 1000:
                print "WIN %d,%d,%d" % (a,b,c)
                if a > 0 and b > 0 and c > 0:
                    print a*b*c


