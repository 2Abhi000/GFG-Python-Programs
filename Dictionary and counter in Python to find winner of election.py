#  Dictionary and counter in Python to find winner of election
s=input()
d={}
for i in s.split():
    d[i]=s.count(i)
#print(max(d.values()))
# prints the key with max no. of occurence
for i in d:
    if(d[i]==max(d.values())):
        print(i)
