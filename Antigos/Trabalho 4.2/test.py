n = input()
x = pow(n,0.5)
auxiliarx = x%1
x = x - auxiliarx
print x
while((pow(x,2)-n)<0):
    x = x + 1
    print x
