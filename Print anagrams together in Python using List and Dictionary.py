#Print anagrams together in Python using List and Dictionary

#Note: I have implemwnted with using list only
s=int(input("Enter the size of array of anagrams: "))
l=[]
for i in range(s):
    l.append(input())
print(l)
c=[]
def prana(a):
    k=a[:]
    #this loop checks for words of string present in another array
    for j in range(len(a)):
        for m in range(len(k)):
            if(a[j][:] in k[m][:]):
                    c.append(k[m])
    #this loop checks for reverse of string in another array
    for j in range(len(a)):
        for m in range(len(k)):
            if(len(a[j])==len(k[m]) and a[j]==k[m][::-1]):
                c.append(k[m])
    print("The list of anagrams are: "list(set(c)))


prana(l)

