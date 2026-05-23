def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n_terms = 10
print(f"Deret Fibonacci {n_terms} angka pertama:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
