#Possible Words using given characters in Python
d=["go","bat","me","eat","goal","boy", "run"]
c=['e','o','b', 'a','m','g', 'l']
n=[]
#append opposite to given word
for i in d:
    for j in i:
        if(j in c):
            pass
        else:
            n.append(i)

#print(n)
#stores original answer
for i in n:
    if(i in d):
        d.remove(i)
#print(d)
for i in d:
    print(i,end=' ')
