n = input ()
auxiliar1 = n
auxiliar2 = n
index = 0
while (auxiliar2!=0):
    if (auxiliar1%auxiliar2==0):
        auxiliar2 = auxiliar2 - 1
        index = index + 1
    else:
        auxiliar2 = auxiliar2 - 1
print index
