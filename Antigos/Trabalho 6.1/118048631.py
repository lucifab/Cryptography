n = input()
while (n>0):
    a,b,modulo = input()
    #trabalhando com a
    if (a<0):
        aauxiliar = -1*a
        if (aauxiliar%modulo != 0):
            naquociente = aauxiliar//modulo + 1
            moduloa = naquociente * modulo - aauxiliar
        else:
            moduloa = 0
    else:
        moduloa = a%modulo

    #trabalhando com b    
    if (b<0):
        bauxiliar = -1*b
        if (bauxiliar%modulo != 0):
            nbquociente = bauxiliar//modulo + 1
            modulob = nbquociente * modulo - bauxiliar
        else:
            modulob = 0 
    else:
        modulob = b%modulo

    #trabalhando com a diferenca
    diferenca = a-b
    if (diferenca<0):
        dauxiliar = -1*diferenca
        if (dauxiliar%modulo != 0):
            ndquociente = dauxiliar//modulo + 1
            modulod = ndquociente * modulo - dauxiliar
        else:
            modulod = 0
    else:
        modulod = diferenca%modulo
    
               
    print moduloa, modulob,(moduloa+modulob)%modulo, modulod%modulo,(moduloa*modulob)%modulo
    print "---"
    n = n-1
 
