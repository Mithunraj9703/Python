list=[1,4,7,9,23,56,78,25,60,100]
i=0
b=0
a=int(input("enter the element:"))
"""while(i<len(list)):
    if(list[i]==a):
        print(a,"get in list at index ",i)
        b+=1
        break
    i+=1
if(b==0):
    print(a,"does not get in list")"""

for el in list:
    if(el==a):
        print(a,"is found in list")
        b+=1
        break
if(b==0):
    print(a,"is not found in list")