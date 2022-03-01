#Remove multiple elements from a list in Python
try:
    
    ar=[]
    n=int(input("Enter the size of array: "))
    for i in range(n):
        ar.append(int(input()))
    print("Array is: ",ar)
    print("Which method you want to choose to remove elements in array: ")

    print("1. By range")
    print("2. By Giving no.")
except ValueError as e:
    print("Error- Invalid No. Entered")
    print("Program Terminated")
    exit()



try:
    me=input("Choose the method: ")
    if(me=='1'):
        r1=int(input("Enter the starting range: "))
        r2=int(input("Enter the ending range: "))
        for i in range(r1,r2+1):
            ar.remove(i)
        print(ar)
    if(me=='2'):
        n1=int(input("Enter the size of no: "))
        ne=[]
        for i in range(n1):
            ne.append(int(input()))
        print("Elements To Remove: ",ne)
        ar = [ele for ele in ar if ele not in ne]
        print("After Removing elements: ",ar)
    else:
        print("Error- Invalid No. Entered")
        print("Program Terminated")
        exit()
except:
    pass
