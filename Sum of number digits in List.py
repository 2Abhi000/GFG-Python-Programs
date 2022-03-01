# Sum of number digits in List
li=[]
n=int(input("Enter the size of list: "))
for i in range(n):
    li.append(int(input()))
l=[]
s=0
for i in li:
    s=0
    for j in str(i):
        s=s+int(j)
    l.append(s)
print("Duplicates elements in list are: ",l)

