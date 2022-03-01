#python tips and tricks
#-----------------------------------------list comprehension---------------------------------
num=[1,2,3,4,5,6,7,8,9,100]
l=[x for x in num if x%2==0]
k=[2**m for m in num]
words=['audio', 'mobile','dog']
words=[word.upper() if word.startswith('a') else word for word in words]
print(words)
print(k)
print(l)
#------------------------------------------------------------------------------------------------

#---------------------------------------string formatting-------------------------------------------
name='Abhishek'
age=22
#method 1
print("Hello my name is "+name+" and I am "+str(age)+" years old!")
#method 2
print("Hello my name is %s and I am %d years old!"%(name,age))
#method 3
print("Hello my name is {0} and I am {1} years old!".format(name,age))
#method 4
print(f"Hello my name is {name} and I am {age} years old!")

#--------------------------------------------------------------------------------------------------------

#---------------------------------------map function------------------------------------------------------
#method 1
numb=[1,2,3,14,5]
def sq(x):
    return x*x
new=[]
for i in numb:
    new.append(sq(i))
print(new)
#method 2
a=[sq(i) for i in numb]
print(a)
#method 3
mo=map(sq,numb)
print(list(mo))
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------Ternary operator----------------------------------------------------
#method 1
agee=12
if agee>18:
    adult=True
else:
    adult=False

if(adult):
    print("Vote")
else:
    print("Not Allowed")
#method 2
ageee=12
adultt=True if ageee>18 else False

if(adultt):
    print("Vote")
else:
    print("Not Allowed")
#---------------------------------------------------------------------------------------------------------------

#------------------------------------------------------Lambda & filter function-----------------------------------------------
#method 1
mysq=lambda x: x*x
print(mysq(5))
#method 2
mysqq=lambda x,y: x+y
print(mysqq(5,2))
#method 3
mys=lambda *x:sum(x)
print(mys(5,10,5))
#method 4
ma=print((lambda x: x**3)(3))
#method 1
nom=[1,4,5,7,8,6,3,22]
eve=list(filter(lambda x: x%2==0,nom))
print(eve)
#----------------------------------------------------------------------------------------------------------------

#---------------------------------------------Enumeration---------------------------------------------------------
#method 1
names=['A','Bhis','Hek','Rishiksa','Abhishek']
co=0
for name in names:
    print(f'{co}:{name}')
    co+=1
#method 2
for index,name in enumerate(names):
    print(f'{index}:{name}')
#method 3
print(list(enumerate(names)))
#----------------------------------------------------------------------------------------------------------------

#--------------------------------------------Reverse list methods----------------------------------------------------
#method 1
val=[1,2,3,4,5,6,78,8,9]
v1al=[2,3,4,5,6,78,8,9]
v2al=[3,4,5,6,78,8,9]
val4=[45,6,5632,4,484,6,46]
re=[]
for index in range(len(val)):
    re.append(val[len(val)- index-1])
print(re)
#method 2
v1al.reverse()
print(v1al)
#method 3
bn=list(reversed(v2al))
print(bn)
#method 4
print(val4[::-1])
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------Docstrings--------------------------------------------
#method 1
def fu():
    '''
this methos prints that ever written inside it
'''
    print("written")

print(help(fu))
#method 2
print(fu.__doc__)
#--------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------Swap values--------------------------------------------------
#method 1
aa=4
bb=5
print("Original: ",aa,bb)
aa=aa^bb
bb=bb^aa
aa=aa^bb
print("Swapped: ",aa,bb)
#method 2
c=7
d=2
c,d=d,c
print(c,d)
#-------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------Merge Dictionay-------------------------------------------
#method 1
d1={1:10,2:20}
d2={3:30,4:40}
print(d1,d2)
d1.update(d2)
d4={5:50,6:60}
#method 2
d5={**d1,**d4}
print("Merge",d1)
print(d5)
#method 3
d6={1:56,8:47}
d7=dict(d6.items() | d4.items())
print(d7)
#------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------MAx function------------------------------------------------------
kl=[1,2,3,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,1,1,3,4]
print(max(kl))
print(max(kl,key=kl.count))
#------------------------------------------------------------------------------------------------------------------
