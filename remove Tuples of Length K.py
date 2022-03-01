#remove Tuples of Length K
#list to tuple
n=int(input("Enter the size of the tuple:"))
a=[]
for i in range(n):
    a.append(tuple(map(int,input().split())))
print("Original tuple: ",list(a))
k=int(input("Enter the length of tuple to remove: "))
for i in a:
    if(len(i)==k):
        a.remove(i)
print(a)
