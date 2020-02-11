
def fatoracao_ingenua(numero):
    potencia = 0
    fator = 2
    vetor = []
    if (numero>=2):
        while (numero>1)or(fator<pow(numero,0.5)):
            if (numero%fator==0):
                while (numero%fator==0):
                    numero = numero/fator
                    potencia = potencia + 1
                print fator, potencia
                vetor.insert(len(vetor),fator)
                fator = fator + 1
                potencia = 0
            else:
                fator = fator + 1
    else:
        print "O numero fatorado deve ser maior ou igual a 2"
    return vetor

n = input ()
while (n!=0):
    a = input()
    vector = []
    vector = fatoracao_ingenua(a)[:]
    i = 0
    arg = False
    while (i<len(vector)):
        c = vector[i]
        if (a%(c*c)==0) or ((a-1)%(c-1)!=0) or (a==c):
            print "NAO"
            arg = True
            break
        i = i + 1
    if arg is False:
        print "SIM"
    print "---"
    n = n - 1
