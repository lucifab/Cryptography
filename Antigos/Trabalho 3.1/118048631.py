n = input()
while (n>0):
    a,b = input()
    q = a//b
    xo = 1
    xi = 0
    yo = 0
    yi = 1
    if (a!=0)and(b!=0):
        print a,"- 1 0"
        print b,"- 0 1"
        while (b>0):
            ''' operacoes de divisao  '''
            d = b
            b = a%b
            a = d
            if (b!=0):
                ''' operacoes entre x e y'''
                dummyx = xi
                dummyy = yi
                xi = xo - q*xi
                yi = yo - q*yi
                xo = dummyx
                yo = dummyy
                '''fim operacoes x e y'''
                print b,q,xi,yi
                q = a//b
            else:
                print b,q,"- -"
        print "---"
    else:
        print "Nao pode botar zero :)"
    n = n-1
"---"
