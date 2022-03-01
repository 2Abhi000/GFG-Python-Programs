# Convert key-values list to flat dictionary
d={}
d1={}
n=int(input("Enter the size of dict 1: "))
for i in range(n):
    k=input("Enter the key: ")
    d[k]=list(map(str, input("Enter the value: ").split()))
print("dictionary 1: ",d)

l=[]
l1=[]

for i in d.values():
    l1.append(i)


for i in l1[0]:
    for j in l1[1]:
        d1[i]=j
        
for i in d1:
    if(i==l1[0][0]):
        d1[i]=l1[1][0]
    if(i==l1[0][1]):
        d1[i]=l1[1][1]
    if(i==l1[0][2]):
        d1[i]=l1[1][2]
print("Flat Dictionary: ",d1)
