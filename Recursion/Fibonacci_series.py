cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f1 = fibonacci(n - 1)
        f2 = fibonacci(n - 2)
        cache[n] = f1 + f2
        return cache[n]

n = int(input("Enter the Fibonacci number: "))
print(fibonacci(n))
print(cache)
