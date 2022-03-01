#Python Dictionary to find mirror characters in a string
a=input("Enter string: ")
ar=[]
ar1=[]
#for extracting all alhabets in small caps
for i in range(95,95+36):
    ar.append(chr(i))
for i in range(2,28):
    ar1.append(ar[i])
#print(ar1)
ar2=[]
#appends alphabets a to m into array ar2 
for i in range(13):
    ar2.append(ar1[i])
ar3=[]
#appends alphabets z to n into array ar3 
for kk in range(13,len(ar1)):
    ar3.append(ar1[kk])
#print(ar1)
#print(ar2)
#reverse the array ar3 to get sorted according to n to z
ar3=ar3[::-1]
#print(ar3)
su=''
su1=''
#adds alphabets a to m into string format for easyness
for lk in ar2:
    su=su+lk
#adds alphabets n to z into string format easyness
for nj in ar3:
    su1=su1+nj
no=int(input("Enter the position to replace: "))
s1=slice(0,no-1)
s2=slice(no-1,len(a))
#stores the string after given position 
io=a[s2]
#print(io)
#stores the string before given position
#print(a[s1])
d1={}
#adds all alphabets from a to m and n to z in a key value pair
for i in range(len(ar2)):
    d1[ar2[i]]=ar3[i]
for ui in range(len(ar3)):
    d1[ar3[ui]]=ar2[ui]
#print(d1)
replaced=''
#if the matching alphabets is found in dictionary then it replaces with is mirror alphabets
for i in io:
    if(i in d1.keys()):
        replaced=replaced+d1[i]
#print(replaced)
#contains desired output
now_new_string=a[s1]+replaced
print(now_new_string)


