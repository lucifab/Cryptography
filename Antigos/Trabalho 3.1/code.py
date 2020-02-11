print "qnts vezes fazer a operacao?"
n = input()
while (n>0):
    print "escolha 2 nums"
    a,b = input()
    q = a//b
    yolo = a
    swag = b
    xo = 1
    xi = 0
    yo = 0
    yi = 1
    print a,"- 1 0"
    print b,"- 0 1"
    if (a!=0)and(b!=0):   
        while (b>0):
            d = b
            b = a%b
            a = d
            if (b!=0):
                ''' parte dos x e dos y'''
                dummyx = xi
                dummyy = yi
                xi = xo - q*xi
                yi = yo - q*yi
                xo = dummyx
                yo = dummyy
                '''fim dessa parte escrota de x e y'''
                print b,q,xi,yi
                q = a//b
            else:
                print b,q,"- -"
        print "---"
    else:
        print "Nao pode botar zero :)"
    n = n-1
"---"
