
# List of string 
list1 = [1,2, 3, 4, 5, 6]

# List of string
list2 = [1 , 2, 3]

'''    
    check if list1 contains all elements in list2
'''
result =  all(elem in list1  for elem in list2)
 
if result:
    print"Yes, list1 contains all elements in list2"    
else :
    print"No, list1 does not contains all elements in list2"
