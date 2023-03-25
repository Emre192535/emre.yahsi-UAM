def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(1))  
print(factorial(2))  
print(factorial(3))  
print(factorial(10))  
print(factorial(32))  