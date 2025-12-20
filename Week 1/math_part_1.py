def fibonacci_series(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def factorial(n):
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value

n = int(input("Enter a number: "))

print("Fibonacci:", fibonacci_series(n))
print("Factorial:", factorial(n))
