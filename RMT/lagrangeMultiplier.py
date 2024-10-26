# Lagrange Multiplier Method :-
from sympy import *
x,y,l=symbols('x,y,l')

objective_fun=input("Enter the objective function: ")
constraint_fun=input("Enter the solve constrant function: ")
object_fun=sympify(objective_fun)
const_fun=sympify(constraint_fun)
fun=object_fun+const_fun

print("exoression: {}".format(fun))
diff_x=Derivative(fun, x)
print("derivation wrt x: {}".format(diff_x.doit()))
diff_y=Derivative(fun, y) 
print("derivation wrt y: {}".format(diff_y.doit()))
diff_l=Derivative(fun, l)
print("derivation wrt l: {}".format(diff_l.doit()))
fx=diff_x.doit()
fy=diff_y.doit()
fl=diff_l.doit()

print("Values of 3 unknown variable are as follows:") 
solutions=solve({fx, fy, fl}, (x, y,l))
print(solutions)
if solutions:
    if isinstance(solutions,dict):
        solution=solutions
    else:
        solution=solutions[0]

x_val=solution[x]
y_val=solution[y]

diff_x_x=Derivative(fx, x)
diff_x_y=Derivative(fx, y)
diff_y_x=Derivative(fy, x)
diff_y_y=Derivative(fy, y)
diff_l_x=Derivative(fl, x)
diff_l_y=Derivative(fl, y)
fxx=diff_x_x.doit()
fxy=diff_x_y.doit()
fyx=diff_y_x.doit()
fyy=diff_y_y.doit()
gx=diff_l_x.doit()
gy=diff_l_y.doit()

H=gx*(fxx*fyy-fyx*fxy)-gy*(fxx*gy-gx*fxy)
if(H<0):
    print("H = ",H)
    print("H is negative so Zmin = ",object_fun.subs({'x':x_val,'y':y_val}))
else:
    print("H = ",H)
    print("H is positive so Zmax = ",object_fun.subs({'x':x_val,'y':y_val}))