print "numero de vezes a operacao ser executada"
n = input()
print "numero um, numero dois, e modulo"

while (n>0):
    a,b,modulo = input()
    if (a>b):
        diferenca = a-b
    else:
        diferenca = b-a
    print a%modulo, b%modulo, (a+b)%modulo, diferenca%modulo,(a*b)%modulo
    print "---"
    n = n-1
print "fim programa"    
