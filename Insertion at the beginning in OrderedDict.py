# Insertion at the beginning in OrderedDict
d={}
d1={}
n=int(input("Enter the size of dict 1: "))
for i in range(n):
    k=input("Enter the key: ")
    d[k]=input("Enter the value: ")
print("dictionary 1: ",d)
n1=int(input("How many items you want to insert into the dict: "))
for i in range(n1):
    k=input("Enter the key: ")
    d1[k]=input("Enter the value: ")
print("Item to be inserted: ",d1)

l=[]
l1=[]

d2={}
d2=d.copy()
d.clear()
d1.update(d2)
print("Insertion at the beginning in OrderedDict: ",d1)
