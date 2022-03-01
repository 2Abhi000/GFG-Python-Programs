#Keys associated with Values in Dictionary
from collections import defaultdict
t = {'abc':[10,30], 'bcd':[30, 40, 10]}
d=defaultdict(list)
print(t)
k=[]
for i,v in t.items():
    for j in v:
        d[j].append(i)
print(str(dict(d)))

