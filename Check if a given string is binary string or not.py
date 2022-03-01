#Check if a given string is binary string or not
s=input("Enter the string: ")
res = ""
#storing all alphabets
for idx in range(97, 97 + 36):
       res = res + chr(idx)
for idx in range(65, 65 + 36):
       res = res + chr(idx)
k=str(res)
for i in s:
    if(i in k):
        print("Invalid")
        break
else:
    print("Valid")

