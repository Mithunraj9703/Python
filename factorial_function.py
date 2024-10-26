def factorial(n):
    a=1
    for i in range(1,n+1,1):
        a*=i
    return a
    
print(factorial(4))
print(factorial(5))
print(factorial(6))