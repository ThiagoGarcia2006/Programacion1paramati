def factorial(n: int)->int:
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n-1) 

    return fact

numero = 5

print(factorial(numero))       