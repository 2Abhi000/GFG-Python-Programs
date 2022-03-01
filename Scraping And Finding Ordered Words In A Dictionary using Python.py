#Scraping And Finding Ordered Words In A Dictionary using Python
a=[]
inp=input()
for i in range(95,95+36):
    a.append(chr(i))
ind=a.index('a')
ind1=a.index('z')

k=slice(ind,ind1+1)
c=a[k]
d={}
for i in c:
    d[i]=c.index(i)
#print(d)

li=[]
for j in inp:
    li.append(j)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(ord(li[i])>ord(li[j])):
            print("Word is not ordered")
            exit()
else:
    print("Word is ordered")
