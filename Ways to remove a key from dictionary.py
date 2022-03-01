#Ways to remove a key from dictionary
d={}
n=int(input("Enter the size: "))
for i in range(n):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    d[k]=v
print("original dictionary ",d)
inp=input("Enter the key to remove: ")
if(inp in d):
    del d[inp]
print("After removing key: ",d)
    
