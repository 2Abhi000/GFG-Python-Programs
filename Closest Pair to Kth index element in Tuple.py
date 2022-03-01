#Closest Pair to Kth index element in Tuple
#list to tuple
n=int(input("Enter the size of the tuple:"))
a=[]
for i in range(n):
    a.append(tuple(map(int,input().split())))
print("Original tuple: ",tuple(a))
k=[]
n1=int(input("Enter the size of the tuple:"))
b=[]
for il in range(n1):
    b.append(tuple(map(int,input().split())))    
print("Tuple elements to search: ",tuple(b))
#logic
for i in a:
    for k in list(i):
        #print(k)
        for j in b:
            for p in list(j):
            #print(p)
                if(k == p):
                    print(i)


