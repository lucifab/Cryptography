n = input()
while (n>=1):
    a,b = input()
    print a
    print b
    c = a%b
    print c
    while (c>0):
        d = c
        c = b%c
        b = d
        print c
    print "---"
    n = n-1
