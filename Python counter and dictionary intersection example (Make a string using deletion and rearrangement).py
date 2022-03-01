#Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
n=input("Enter the string: ")
n1=input("Enter the another string: ")
#if we find all the string of s1 into s2 string then we can simply write the logic to generate the string 
for i in n:
    if(i in n1):
        t=1
    else:
        t=0
if(t):
    print("Possible")
else:
    print("Not Possible")
