import math
import numpy as np

print "Ate que numero voce deseja encontrar primos?"
n = input()
vetor = range(n+1)
del vetor[0]
print "O seu vetor e",vetor
i = 2
p = 2
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
    while (p<=vetormestre[n-1]):
        if p in vetor:
            vetor[p-1] = 0
            cortes = True
            if (primeiro<1):
                primeirovalor = p
                primeiro = primeiro + 1
                
            
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

        
    
    
