a=int(input("enter the 1st value:= "))
b=int(input("enter the 2nd value:= "))
c=int(input("enter the 3rd value:= "))
if(a>b):#if(a>b and a>c):
    if(a>c):
        print("greatest value := ",a)
    else:
        print("greates value := ",c)
else:
    if(b>c):
        print("greatest value:= ",b)
    else:
        print("greatest value:= ",c)