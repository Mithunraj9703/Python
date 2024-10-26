dict={}
a=int(input("enter the 1st subject marks:"))
b=int(input("enter the 2nd subject marks:"))
c=int(input("enter the 3rd subject marks:"))
dict.update({"sub1":a})
dict.update({"sub2":b})
#dict.update({"sub3":c})
dict["sub3"]=c
print(dict)