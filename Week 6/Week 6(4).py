# Factorial using lambda (recursive)
factorial = lambda n: 1 if n == 0 or n == 1 else n * factorial(n - 1)

# Example usage
num = 10
print("Factorial of", num, "is:", factorial(num))
