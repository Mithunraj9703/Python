import math
import sympy as sp
from sympy import *
x,y,l=symbols('x,y,l')
# f=x+y
# z=lambda x,y:(f(x,y))
# print(z(2,3))
of=lambda x,y: eval(input("Enter objective function: "))
# x=3
# y=2
# print(of)
# cf=lambda x,y: eval(input("Enter constraint function: "))
# z=lambda x,y,l:(of(x,y)+l*(cf(x,y)))
# print(z(1,2,3))
# exp=str(z)
# print(exp)

print("exoression: {}".format(of))
# diff_x=Derivative(z, x)
# print("derivation: {}".format(diff_x.doit()))
# diff_y=Derivative(z,y)
# diff_l=Derivative(z,l)
# eq1 = Eq((diff_x), 0) 
# eq2 = Eq((diff_y), 0) 
# eq3 = Eq((diff_l), 0) 
# print("Values of 3 unknown variable are as follows:") 
# print(solve((eq1, eq2, eq3), (x, y,l))) 
