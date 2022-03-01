#Handling missing keys in Python dictionaries
n=int(input("Enter the size of dictionary: "))
d={}
for i in range(n):
    
    k=input("Enter the Key: ")
    v=input("Enter the value: ")
    d[k]=v
l=[]
k=[]

kee=input("Enter the key to find: ")

def fin():
    if(kee not in d):
        print("This key is not in dictionary")
    else:
        print("Value with the associated key: ",d[kee])

fin()
