#Maximum and Minimum K elements in Tuple
n= int(input())
t=[]
for i in range(n):
    t.append(input())
k=int(input("Enter the no. of max and min "))
x=tuple(t)
#print(x)
s=sorted(x)
sn=str(x[:k])
l=str(x[-k:])
print(l+sn)
