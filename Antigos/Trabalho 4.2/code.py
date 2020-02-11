print "Numero de vezes que a operacao sera executada"
n = input()
i = 0
while (i<n):
    print "Numero que sera submetido ao algoritmo de Fermat"
    numero = input()
    ###achando primeiro x e o arredondando
    x = pow(numero,0.5)
    auxiliarx = x%1
    x = x - auxiliarx
    ###condicao se n for quadrado perfeito
    if (numero==pow(x,2)):
                print int(x),int(y),"S"
    ###caso contrario    
    else:
        print int(x),"0 N"
        ##raiz real
        while((pow(x,2)-numero)<0):
            x = x + 1
        y = pow(x,2)- numero
        y = pow(y,0.5)
        ##arredondando y
        auxiliary = y%1
        y = y - auxiliary
        ##fim arrend. y
        condicao = ((numero+1)/2)
        expressao = (pow(x,2)- pow(y,2))
        while (expressao!=numero):
                expressao = (pow(x,2)- pow(y,2))
                if(expressao != numero):
                    print int(x),int(y),"N"
                    x = x + 1
                    y = pow(x,2)- numero
                    y = pow(y,0.5)
                    ##arredondando y
                    auxiliary = y%1
                    y = y - auxiliary
                    ##fim arrend. y

        print int(x),int(y),"S"
        a = x+y
        b = x - y
        print int(b),int(a)
        i = i+1
    print "---"
print "Fim do programa"
