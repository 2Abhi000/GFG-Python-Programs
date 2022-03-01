#Python program to find uncommon words from two Strings
s=input("Enter the string 1: ")
s1=input("Enter the string 2: ")
c=[]
for i in s1.split():
    if(i not in s):
        c.append(i)
for j in s.split():
    if(j not in s1):
        c.append(j)
print(c)
