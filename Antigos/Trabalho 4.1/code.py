print "Numero de vezes que a operacao sera executada"
n = input()
i = 0
while (i<n):
    print "Numero que deseja ser fatorado"
    numero = input()
    potencia = 0
    fator = 2
    if (numero>=2):
        while (numero>1):
            if (numero%fator==0):
                while (numero%fator==0):
                    numero = numero/fator
                    potencia = potencia + 1
                print "Fator // Potencia"
                print fator, potencia
                fator = fator + 1
                potencia = 0
            else:
                fator = fator + 1
        print "---"
        i = i+1
    else:
        print "O numero fatorado deve ser maior ou igual a 2"
print "Fim do programa"
