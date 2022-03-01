#Remove empty List from List
li=[1,[],8,[],9]
k=[]
for i in li:
    if(k in li):
        li.remove(k)
print(li)
