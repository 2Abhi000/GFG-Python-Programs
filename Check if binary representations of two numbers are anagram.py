#Check if binary representations of two numbers are anagram
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
#prints binary on a number
x=(bin(a))
y=(bin(b))
#print("Binary of {0} is {1}: ".format(a,x))
#print("Binary of {0} is {1}: ".format(b,y))
c=0
c1=0
v=0
v1=0
#count the no. of 1s and 0s in both no.
for i in x:
    if(i=='0'):
        c=c+1
    elif(i=='1'):
        c1=c1+1
    else:
        pass
for i in y:
    if(i=='0'):
        v=v+1
    elif(i=='1'):
        v1=v1+1
    else:
        pass
#print("No. of zeros is={0} & No. of one is={1} in {2} ".format(c,c1,a))
#print("No. of zeros is={0} & No. of one is={1} in {2} ".format(v,v1,b))
#function to check if both no. contains same no. of 1s or 0s
def countt(j,k,l,m):
    if(c==v or c1==v1):
        print("Yes")
    else:
        print("No")

countt(c,v,c1,v1)

