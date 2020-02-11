#Definindo as funcoes


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
        mdc = (xi*ao)+(yi*bo)
        #O xi eh o alfa e o yi eh o beta!
    return mdc,xi
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

vetor_a,vetor_b=input()
i = 0

print "Seus vetores sao",vetor_a,vetor_b
while (i<(len(vetor_a)-1)):
    mdc,alfa = algoritmo_euclidiano(vetor_b[i],vetor_b[i+1])
    print "O mdc eh",mdc,";O alfa eh",alfa
    if (mdc==1):
        aux1a = (vetor_a[i+1] - vetor_a[i])*alfa
        aux1b = mod(aux1a,vetor_b[i+1])
        aux2 = vetor_b[i]*vetor_b[i+1]
        aux1b = (aux1b*vetor_b[i])+vetor_a[i]
        vetor_a[i+1] = aux1b
        vetor_b[i+1] = aux2
        print "A congruencia eh",vetor_a[i+1],vetor_b[i+1]
        i =  i+1


    else:
        print "Nao eh possivel fazer esta porra :^)"
        quit()
        quit()
print "---"
