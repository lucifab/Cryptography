def algoritmo_euclidiano(a,b):
    ao = a
    bo = b
    xo = 1
    xi = 0
    yo = 0
    yi = 1
    if (a!=0)and(b!=0):
        q = a//b
        print a,"- 1 0"
        print b,"- 0 1"
        while (b>0):
            ''' operacoes de divisao// division operations  '''
            d = b
            b = a%b
            a = d
            if (b!=0):
                ''' operacoes entre x e y // operations between x and y'''
                dummyx = xi
                dummyy = yi
                xi = xo - q*xi
                yi = yo - q*yi
                xo = dummyx
                yo = dummyy
                '''fim operacoes x e y // end op. x and y'''
                print b,q,xi,yi
                q = a//b
            else:
                print b,q,"- -"
        mdc = (xi*ao)+(yi*bo)
        #O xi eh o alfa e o yi eh o beta!
    return mdc,xi,yi
#Fim algoritmo_euclidiano

def mod(x,z):
    if (x<0):
        aauxiliar = -1*x
        if (aauxiliar%z != 0):
            naquociente = aauxiliar//z + 1
            moduloa = naquociente * z - aauxiliar
        else:
            moduloa = 0
    else:
        moduloa = x%z
    return moduloa
#Fim funcao mod
#chinese remainder theorem
def algoritmo_chines(vetor_a,vetor_b):
    #O vetor_a  eh o vetor que contem a parte direita da equacao modular
    #exemplo
    # x = vetor_a[i] (mod vetor_b[i])
    #funciona para quantos forem o numero de equacoes modulares!
    i = 0

    while (i<(len(vetor_a)-1)):
        mdc,alfa,beta = algoritmo_euclidiano(vetor_b[i],vetor_b[i+1])
        print alfa,beta
        if (mdc==1):
            aux1a = (vetor_a[i+1] - vetor_a[i])*alfa
            aux1b = mod(aux1a,vetor_b[i+1])
            aux2 = vetor_b[i]*vetor_b[i+1]
            aux1b = (aux1b*vetor_b[i])+vetor_a[i]
            vetor_a[i+1] = aux1b
            vetor_b[i+1] = aux2
            print vetor_a[i+1],vetor_b[i+1]
            i =  i+1
        else:
            quit()
    print "---"
#fim algoritmo_chines
