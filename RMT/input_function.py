from sympy import*
# x,y=symbols('x,y')
function=input("Enter the function: ")
print("Function: ",function)
print("Function: {}".format(function))
fun=sympify(function)
print("Value is ",fun.subs({'x':3,'y':2}))