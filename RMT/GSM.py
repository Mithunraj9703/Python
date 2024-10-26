# Miimize the function f(x)=4x^3+x^2-7x+14 
from sympy import*
x=symbols('x')
function=input("Enter the function: ")
l=int(input("Enter the value of L :- "))
r=int(input("Enter the value of R :- "))
e=float(input("Enter the stopping tolerence :- "))
t=1.618   # t = Golden Ratio
fun=sympify(function)
print("exoression: ",fun)

while((r-l)>=e):
    x2=l+1/t*(r-l)
    x1=l+r-x2
    fx1=fun.subs({'x':x1})
    fx2=fun.subs({'x':x2})
    if(fx1>fx2):
        l=x1
    else:
        r=x2

    if(r-l<e):
        break

print("Xmin = ",round((r+l)/2,3))