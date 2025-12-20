import math

def fibonacci_series(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def factorial_using_math(n):
    return math.factorial(n)

n = int(input("Enter a number: "))

print("Fibonacci:", fibonacci_series(n))
print("Factorial:", factorial_using_math(n))
