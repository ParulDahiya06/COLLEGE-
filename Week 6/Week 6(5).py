# Fibonacci using lambda (recursive)
fibonacci = lambda n: n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# Example: Print first 15 Fibonacci numbers
for i in range(15):
    print(fibonacci(i), end=" ")
