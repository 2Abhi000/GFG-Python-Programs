#  Check order of character in string using OrderedDict( )
s=input()
p=input()
def chek(s,p):
    c=s.count(p)
    if(c==1):
        return True
    #if therir is more then one sequence occuring then retiurn fase
    else:
        return False
print(chek(s,p))
