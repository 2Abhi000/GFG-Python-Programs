#Python program to print all even  and odd numbers in a range
ele=int(input("Enter the starting range: "))
ele1=int(input("Enter the ending range: "))
l=[]
l1=[]
for i in range(ele,ele1):
    if(i%2==0):
        l.append(int(i))
    if(i%2!=0):
        l1.append(int(i))

print("Even elements in given range: ",l)
print("Odd elements in given range: ",l1)

