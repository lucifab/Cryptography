n = input()
i = 0
while (i<n):
    numero = input()
    potencia = 0
    fator = 2
    if (numero>=2):
        while (numero>1)or(fator<pow(numero,0.5)):
            if (numero%fator==0):
                while (numero%fator==0):
                    numero = numero/fator
                    potencia = potencia + 1
                print fator, potencia
                fator = fator + 1
                potencia = 0
            else:
                fator = fator + 1
        print "---"
        i = i+1
    else:
        print "O numero fatorado deve ser maior ou igual a 2"

