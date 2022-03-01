#Python program to create a list of tuples from given list having number and its cube in each tuple
#calculate cube 
def cub(x):
    return x*x*x
n=int(input("Enter the size of the list:"))
a=[]
for i in range(n):
    a.append(int(input()))
k=[]
#logic to implement
for i in a:
    o=cub(i)
    tu=[]
    tu.append(i)
    tu.append(o)
    l=tuple(tu)
    k.append(l)
    
print(k)
