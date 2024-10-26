# using while loop:
"""n=int(input("enter the value of n:"))
i=0
a=0
while i<n:
    i+=1
    a+=i
print(a)"""

#using for loop:
n=int(input("enter the value of n:"))
a=0
for el in range(0,n+1,1):
    a+=el
print(a)