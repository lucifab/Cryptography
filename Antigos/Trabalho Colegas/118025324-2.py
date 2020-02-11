#algoritmo de fatoracao de Fermat
from math import floor, pow, sqrt

n=input()
for i in range(n):
	num=input()
	x=floor(sqrt(num))
	y=0
	while(num!=(pow(x,2)-pow(y,2))):
		print int(x),int(y),"N"
		x+=1
		y=floor(sqrt(pow(x,2)-num))
	print int(x),int(y),"S"
	print int(x-y),int(x+y)
	print"---"


