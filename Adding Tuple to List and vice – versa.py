#Adding Tuple to List and vice – versa
#list to tuple
n=int(input("Enter the size of the list:"))
a=[]
for i in range(n):
    a.append(input())
print("Original list",a)
k=[]
n1=int(input("Enter the size of the tuple:"))
b=[]
for il in range(n1):
    b.append(input())
#logic to implement
for i in b:
    a.append(i)
    
print("The container after addition",tuple(a))
#tuple to list
n=int(input("Enter the size of the tuple:"))
a=[]
for i in range(n):
    a.append(input())
print("Original tuple",tuple(a))
k=[]
n1=int(input("Enter the size of the list:"))
b=[]
for il in range(n1):
    b.append(input())
#logic to implement
for i in b:
    a.append(i)
    
print("The container after addition",list(a))
