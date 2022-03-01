#Counting the frequencies in a list using dictionary in Python
n=int(input("Enter the size of array: "))
s=[]
d={}
print("Enter the value: ")
for i in range(n):
    s.append(input())
s.sort()
for j in s:
    d[j]=s.count(j)
for k,m in d.items():
    print(k,m)
