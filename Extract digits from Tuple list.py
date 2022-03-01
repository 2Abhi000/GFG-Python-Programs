# Extract digits from Tuple list
#list to tuple
n=int(input("Enter the size of the tuple:"))
a=[]
for i in range(n):
    a.append(tuple(map(str,input())))
print("Original tuple: ",list(a))
l=[]
for i in a:
    for j in i:
        l.append(j)
s=list(set(l))
del l
#print(s)
l=[]
for i in s:
    if(i!=' '):
        l.append(i)
l.sort(reverse=True)
print(l)
    
