# # import sympy 
# from sympy import *

# x, y = symbols('x,y')
# expr = x**2 + 2 * y + y**3
# print("Expression : {}".format(expr))

# # Use sympy.Derivative() method 
# expr_diff = Derivative(expr, x) 
	
# print("Derivative of expression with respect to x : {}".format(expr_diff)) 
# print("Value of the derivative : {}".format(expr_diff.doit()))

# x, y = symbols('x,y') 
  
# # defining equations 
# eq1 = Eq((x+y), 1) # x+y=1
# print("Equation 1:") 
# print(eq1) 
# eq2 = Eq((x-y), 1) 
# print("Equation 2") 
# print(eq2) 
  
# # solving the equation 
# print("Values of 2 unknown variable are as follows:") 
  
# print(solve((eq1, eq2), (x, y))) 

# # importing Numpy package 
# import numpy as np 

# # creating a 3X3 Numpy matrix 
# n_array = np.array([[55, 25, 15], 
# 					[30, 44, 2], 
# 					[11, 45, 77]]) 

# # Displaying the Matrix 
# print("Numpy Matrix is:") 
# print(n_array) 

# # calculating the determinant of matrix 
# det = np.linalg.det(n_array) 

# print("\nDeterminant of given 3X3 square matrix:") 
# print(int(det)) 

# take input form list
supply=[]
print("Enter the supply with space separated: ")
for i in range(0):
    const = list(map(float, input().split()))
    supply.append(const)
print(supply)