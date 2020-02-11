import math
import numpy as np

print "Ate que numero voce deseja encontrar primos?"
n = input()

#criando a lista a pulando pares
vetor = []
a=3
while(a<=n):
     vetor.insert(len(vetor),a)
     a+=2

print "O seu vetor e",vetor
i = 3
p = 3
j = 0
m = 0
auxiliar = p
primeiro = 0
#criando lista auxiliar original
vetormestre = vetor[:]
vetorcorte = []
vetorrodada = []

print "O valor que o crivo ira ate sera",int(math.sqrt(n))
print "***"

while (i<=math.sqrt(n)):
    p = pow(p,2)
    
    
    #achando o vetor
    while (p<=vetormestre[-1]):
        if p in vetor:
            if (primeiro<1):
                primeirovalor = p
                primeiro = primeiro + 1
                posicao = vetor.index(p)
            index = vetor.index(p)
            vetor[index] = 0
            cortes = True
        p = p + auxiliar

    if cortes is True:
        
        #lista de primos sem zero
        vetorprimo = []
        for j in range(0,len(vetor)):
            vetorprimo.insert(len(vetorprimo),vetor[j])
        while 0 in vetorprimo:
            vetorprimo.remove(0)


        
        #achando vetor corte

        if (m==0):
            vetorcorte = list(np.array(vetormestre) - np.array(vetor))
            m = 1   

        else:
            vetorcorte = list(np.array(vetorrodada) - np.array(vetor))
            vetorrodada= []
            
        for j in range(0,len(vetor)):
                vetorrodada.insert(len(vetorrodada),vetor[j])
                
        while 0 in vetorcorte:
            vetorcorte.remove(0)
        


        #printando a porra toda
        print "Vetor de lasso",i-1
        print "pulando de",i,"em",i
        print "Primeiro valor a ser cortado", primeirovalor
        print "Posicao do valor", posicao
        print "vetor sem tirar zeros e",vetor
        print "vetor mestre",vetormestre
        print "vetor primo",vetorprimo
        print "vetor corte",vetorcorte

    else:
       print "Nao houveram cortes para o lasso",i
       
    i = i + 1
    p = i
    auxiliar = p
    cortes = False
    primeiro = 0
    print "***"

        
    
    
