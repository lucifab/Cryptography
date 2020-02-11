import math

n = input()


#criando a lista a pulando pares
vetor = []
a=3
while(a<=n):
     vetor.insert(len(vetor),a)
     a+=2


print vetor
i = 3
p = 3
j = 0
m = 0
auxiliar = p
primeiro = 0

#criando lista auxiliar original
vetormestre = vetor[:]
vetorprimo = []

print int(math.sqrt(n))

#excecoes escrotas
if (n<=8):
    vetor = [2] + vetor
    print int(math.sqrt(n)),"* *"
    print vetor


#o negocio pros numeros grandoes

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
        vetorcorte = []
        a = primeirovalor
        while(a<=n):
             vetorcorte.insert(len(vetorcorte),a)
             a = a + 2*i



        #printando a porra toda
        print i,primeirovalor, posicao
        print vetorcorte
        print vetorprimo

    i = i + 1
    p = i
    auxiliar = p
    cortes = False
    primeiro = 0

if (n>8):
    vetorprimo.insert(0, 2)
    print vetorprimo
