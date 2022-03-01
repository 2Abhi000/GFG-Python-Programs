#Program for Find remainder of array multiplication divided by n
ar=[]
el=int(input("Enter the size of matrix: "))
for i in range(el):
    ar.append(int(input()))
no=int(input("Enter the number: "))
m=1
print("Elements in array: ",ar)
for i in ar:
   m=m*i
print("After Multiply: ",m)
print("After Divide: ",m%no)


