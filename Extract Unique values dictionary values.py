#Extract Unique values dictionary values
d={}
n=int(input("Enter the size: "))
for i in range(n):
    d[i]=list(map(int,input().split()))
print("original dictionary ",d)
s=[]
for k in d.values():
    for t in k:
        s.append(int(t))
xx=set(s)
print("Unique values in list",list(xx))
    
