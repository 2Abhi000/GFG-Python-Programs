#Python program for removing i-th character from a string
s=input("Enter the string: ")
k=''
pos=int(input("Enter the position: "))
s1=s[:pos-1]
s2=s[pos:]
print("Removed: ",s1+s2)
