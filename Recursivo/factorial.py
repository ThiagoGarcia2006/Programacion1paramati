
def factorial(n: int)->int:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact    
   


numero = 5

print(factorial(numero))