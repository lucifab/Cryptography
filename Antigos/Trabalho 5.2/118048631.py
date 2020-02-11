n = input()
vetor = []
i = n
auxiliar1 = n
auxiliar2 = n
while (i>0):
    index = 0
    while (auxiliar2!=0):
        if (auxiliar1%auxiliar2==0):
            auxiliar2 = auxiliar2 - 1
            index = index + 1
        else:
            auxiliar2 = auxiliar2 - 1
    vetor.insert(len(vetor),index)    
    i = i - 1
    auxiliar1 = auxiliar1 - 1
    auxiliar2 = auxiliar1
vetor.reverse()

#comparador
final = []
i = n-1
p = 1
while (i>=0):
    arg = True
    while (p<=i):

        if (vetor[i] <= vetor[i-p]):
            arg = False
            break
            
        else:
            p = p + 1
        
    if (arg==True):
      final.insert(len(vetor),i+1)  
    i = i - 1
    p = 1
final.reverse()
print final
