#Remove all duplicates words from a given sentence
a=input("Enter string: ")
k=a.split()
s=''
ss=list(set(k))
p=[]
for i in ss:
    p.append(i)
#print(p)
for j in p:
    print(j,end=' ')
#print(s,ss)
            
