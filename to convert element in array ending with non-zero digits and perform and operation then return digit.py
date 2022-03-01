#to convert element in array ending with non-zero digits and perform and operation then return digit
def binnn(binary): 
    int_val, i, n = 0, 0, 0
    while(binary != 0): 
        a = binary % 10
        int_val = int_val + a * pow(2, i) 
        binary = binary//10
        i += 1
    return(int_val) 
ar=['11','20','10','50']
print("Original Array: ",ar)
for i in ar:
    for j in i[-1]:
        if(j=='0'):
            pass
        else:
            x=bin(int(i))
            z=1 and x
            #a = int(z,2)
            t1=z[-2:]
            a=binnn(int(t1))
            ar[ar.index(i)]=a
ar1=[]
for i in ar:
    ar1.append(int(i))
print("Converted Array: ",ar1)
    

