#Find words which are greater than given length k
s=input("Enter the string: ")
t=int(input("Enter the length: "))
l=s.split()
for i in range(len(l)):
    if(len(l[i])>t):
        print(l[i])
        
    else:
        pass
        

