#Python Counter to find the size of largest subset of anagram words
a=input("Enter anagarams seperated by space: ")
k=a.split()
print(k)
d=[]
for i in k:
    for j in range(len(k)):
        if(len(i)==len(k[j])):
            d.append(int(len(i)))
c={}
for i in d:
    c[i]=d.count(i)
#print(c)
s=max(d)
cc=0
for i in k:
    if(s==len(i)):
        cc=cc+1
print(cc)
    
            
