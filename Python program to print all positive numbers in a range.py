#Python program to print positive numbers in a list
ar=[]
n=int(input("Enter the size of array: "))
for i in range(n):
    ar.append(int(input()))
print("Array is: ",ar)
k=[]
for i in ar:
    if(i>=0):
        k.append(int(i))
print("Positive no. in the array are: ",k)
