#Python program to find the sum of all items in a dictionary
d={}
n=int(input("Enter the size: "))
for i in range(n):
    d[i]=list(map(int,input().split()))
print("original dictionary ",d)
s=[]
for k in d.values():
    for t in k:
        s.append(int(t))
xx=sum(s)
print("Sum is",xx)
    
