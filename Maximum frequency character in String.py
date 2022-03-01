# Maximum frequency character in String
s=input("Enter the string: ")
d={}
for i in s:
    d[i]=s.count(i)
#print(d)
print("Max Frequently character is: ",max(d,key=d.get))
