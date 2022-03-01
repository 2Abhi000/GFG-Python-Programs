#Count occurrences of an element in a list
ar=[]
n=int(input("Enter the size of array: "))
for i in range(n):
    ar.append(int(input()))
print("Elements in array are",ar)
el=int(input("Enter the element to count the no. of occurrences: "))
if(el in ar):
    c=ar.count(el)
print("The no. of time the element {0} occured in list is {1} time".format(el,c))
