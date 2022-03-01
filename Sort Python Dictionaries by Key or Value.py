#Sort Python Dictionaries by Key or Value
n=int(input("Enter the size of dictionary: "))
d={}
for i in range(n):
    
    k=int(input("Enter the Key: "))
    v=input("Enter the Value: ")
    d[k]=v
l=''
k=''
print("On what basis you want to sort your dictionary: ")
print("1. By Key : Press 'k'")
print("2. By Value : Press 'v'")
print("3. By Both : Press 'b'")
ch=input()
def cho(ch):
    if(ch=='k' or ch=='K'):
        #sort by key
        for i in range(len(d)):
            l=(sorted(tuple(d.keys())))
            break
        for i in range(len(d)):
            k=(tuple(d.values()))
            print(list(l)+list(k))
            break
    if(ch=='v' or ch=='V'):
        #sort by value
        for i in range(len(d)):
            l=(tuple(d.keys()))
            break
        for i in range(len(d)):
            k=(sorted(tuple(d.values())))
            print(list(l)+list(k))
            break
    if(ch=='b' or ch=='B'):
        #sort by both
        for i in range(len(d)):
            l=(sorted(tuple(d.keys())))
            break
        for i in range(len(d)):
            k=(sorted(tuple(d.values())))
            print(list(l)+list(k))
            break
cho(ch)

