#Python program to find Cumulative sum of a list
li=[]
n=int(input("Enter the size of list: "))
for i in range(n):
    li.append(int(input()))
l=[]
s=0
for i in li:
    s+=i
    l.append(int(s))
print("Duplicates elements in list are: ",l)

