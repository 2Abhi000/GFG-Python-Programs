#Flatten tuple of List to tuple
n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    k=input("Enter the value: ")
    a.append(list(k))

j=[]
for i in a:
    for l in i:
        j.append(int(l))
print(tuple(j))
