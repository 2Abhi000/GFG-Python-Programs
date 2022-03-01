#Python program to find second largest number in a list
ar=[]
n= int(input("Enter the size of array: "))
for i in range(n):
    ar.append(int(input()))
print("Original array: ",ar)
ar.remove(max(ar))
print("2nd Max element in array is: ",max(ar))
