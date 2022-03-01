#Remove empty tuple from a list
ar=[]
n=int(input("Enter the size of array: "))
for i in range(n):
    ar.append(tuple(input()))
print("Elements is list: ",ar)
for i in ar:
    if(() in ar):
        ar.remove(())
print("After removing the empty tuples from list: ",ar)
