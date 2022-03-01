#Program to print duplicates from a list of integers
li=[]
n=int(input("Enter the size of list: "))
for i in range(n):
    li.append(int(input()))
l=[]
for i in li:
    if(li.count(i) >1):
        l.append(int(i))
k=set(l)
print("Duplicates elements in list are: ",list(k))

