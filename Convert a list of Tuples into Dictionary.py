#Convert a list of Tuples into Dictionary
n=int(input("Enter the size of array: "))
s=[]
d={}
#takes the values in a array
print("Enter the value: ")
for i in range(n):
    s.append(tuple(input().split()))

print("List of tuples: ",s)
#logic to ectract only numeric values form list of tuples
for i in s:
    for j in i:
        if(not j.isalpha()):
            d[i[0]]=int(j)
print("Converted into dictionay: ",d)
