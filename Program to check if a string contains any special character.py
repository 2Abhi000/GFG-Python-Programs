#Program to check if a string contains any special character
s=input("Enter the string: ")
l=['!','@','#','&','$']
t=0
for i in s:
    if(i in l):
        t=0
        break
    else:
        t=1
        
if(t):
    print("String is Accepted")
else:
    print("String is not Accepted")
