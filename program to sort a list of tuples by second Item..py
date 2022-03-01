#program to sort a list of tuples by second Item
#list to tuple
n=int(input("Enter the size of the tuple:"))
a=[]
for i in range(n):
    st=input("Enter the string: ")
    no=int(input("Enter the number: "))
    a.append((st,no))
print("Original tuple: ",list(a))
a.sort(key=lambda x: x[1])
print(a)
