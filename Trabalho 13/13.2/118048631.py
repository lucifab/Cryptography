#definindo funcao multiplicacao em mod
def modprod(x,y,z):
    #trabalhando com x
    if (x<0):
        aauxiliar = -1*x
        if (aauxiliar%z != 0):
            naquociente = aauxiliar//z + 1
            moduloa = naquociente * z - aauxiliar
        else:
            moduloa = 0
    else:
        moduloa = x%z

    #trabalhando com y
    if (y<0):
        bauxiliar = -1*y
        if (bauxiliar%z != 0):
            nbquociente = bauxiliar//z + 1
            modulob = nbquociente * z - bauxiliar
        else:
            modulob = 0
    else:
        modulob = y%z
    return (moduloa*modulob)%z

#definindo algoritmo potenciacao modular
def alg_potenciacao_modular(base,exp,mod):
    r = 1
    A = base
    E = exp

    while (E!=0):
        #argumento se E eh impar ou nao
        if (E%2!=0):
            arg = "S"
        else:
            arg = "N"

        print r,A,E,arg

        #agora o algoritmo em si
        if(E%2!=0):
            r = modprod(r,A,mod)
            E = (E-1)/2
        else:
            E = E/2
        A = modprod(A,A,mod)
    #fim do while

    #argumento se E eh impar ou nao
    if (E%2!=0):
        arg = "S"
    else:
        arg = "N"

    print r,A,E,arg
    return r
#fim potenc.potenciacao_modular_fermat

import math
k = input ()
while (k>0):
    flag = 1

    n = input ()
    mersenne = 2**n - 1
    r = 1
    print mersenne
    max = int((math.pow(2,(float(n)/2))-1)/(2*n))
    print max
    while (r<=max):
        q = 1 + 2*r*n
        print r
        resto = alg_potenciacao_modular(2,n,q)
        if (resto==1):
            #Caso de ser composto
            print q
            flag = 0
            break
        r = r + 1
    if (flag==1):
        #Caso de ser primo
        print mersenne
    print "---"
    k = k - 1