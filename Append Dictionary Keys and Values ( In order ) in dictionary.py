#Append Dictionary Keys and Values ( In order ) in dictionary
n=int(input("Enter the size of dictionary: "))
d={}
for i in range(n):
    
    k=input("Enter the Key: ")
    v=input("Enter the Value: ")
    d[k]=v
l=''
k=''
for i in range(len(d)):
    l=(list(d.keys()))
    break
for i in range(len(d)):
    k=(list(d.values()))
    break
print(l+k)
