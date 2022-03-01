# Sort Dictionary key and values List
n=int(input("Enter the size of dictionary: "))
d={}
for i in range(n):
    
    k=input("Enter the Key: ")
    v=list(map(int,input("Enter the Value: ").split()))
    d[k]=v
l=[]
k=[]


def cho():
    #sort by both
    for i in range(len(d)):
        l.append(sorted(d.keys()))
        #print(l)
        break
    for j in d.values():
        k.append(sorted(j))
    #print(k)
cho()
#print(l)
#print(k)
d1=[]
k=k[::-1]
for i in range(len(l[0])):
    for j in range(len(k)):
        
        d1.append(str(l[0][i])+str(k[i]))

c1=[]
# i have printed in list format instead of dictionary but the output format was same
for i in range(0,len(d1),3):
    c1.append(d1[i])
print(c1)

