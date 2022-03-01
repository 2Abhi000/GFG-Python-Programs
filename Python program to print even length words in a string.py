#Python program to print even length words in a string
st=input()
st=st.split()
for i in st:
    if(len(i)%2==0):
        print(i)
