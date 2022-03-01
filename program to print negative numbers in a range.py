#Python program to print negative numbers in a range
ar=[]
n=int(input("Enter the starting range of array: "))
n2=int(input("Enter the ending range of array: "))
for i in range(n,n2):
    ar.append(int(i))
print("Array is: ",ar)
k=[]
for i in ar:
    if(i<0):
        k.append(int(i))
print("Negative no. in the range are: ",k)
