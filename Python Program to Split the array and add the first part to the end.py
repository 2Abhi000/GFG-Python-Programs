#Python Program to Split the array and add the first part to the end
ar=[]
el=int(input("Enter the size of matrix: "))
for i in range(el):
    ar.append(input())
ind=int(input("Enter the position: "))
s=''
s1=''
for i in ar:
    s1=s1+str(i)

l=[]

for i in ar:
    if(ar.index(i)==ind):
        break
    else:
        s=s+str(i)
x=''
x=s1[ind+2:]+s
print(x)



