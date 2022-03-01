#Merging two Dictionaries
d={}
d1={}
n=int(input("Enter the size of dict 1: "))
for i in range(n):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    d[k]=v
print("dictionary 1: ",d)
n2=int(input("Enter the size of dict 2: "))
for i in range(n2):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    d1[k]=v
print("dictionary 2: ",d1)
def mer(d,d1):
    return(d.update(d1))
    
mer(d,d1)
print("After merge dictionary is : ",d)
