#algoritmo ingenuo de fatoracao
from math import floor, sqrt

n=input()
for i in range (n):
	x=input()
	raiz=floor(sqrt(x))
	f=2
	while(f<=raiz):
		cont=0
		while(x%f==0):
			cont+=1
			x/=f
		if (cont>0):
			print f, cont
		f+=1
	if(x>1):
		print x,1
	print "---"