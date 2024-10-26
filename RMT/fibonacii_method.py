# Minimize the equation:- (fx)=x^2 n=3 (0,1) 
from sympy import*
x=symbols('x')
function=input("Enter the function: ")
l=int(input("Enter the value of L : "))
r=int(input("Enter the value of R : "))
n=int(input("Enter the no. of iteration : "))
k=int(input("Enter the value of K : "))

fun=sympify(function)
print("exoression: ",fun)
# print(fun)

fibo=[1,1,2,3,5,8]
while(k<n):
    fk=round((fibo[n-k]/fibo[n-k+1]),3)
    x2=l+fk*(r-l)
    x1=l+r-x2
    fx1=fun.subs({'x':x1})
    fx2=fun.subs({'x':x2})
    if(fx1>fx2):
        l=x1
    else:
        r=x2
    k+=1
    if(k==n):
        break
print("Xmean = ",round((r+l)/2,3))