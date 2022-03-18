def fibonacci_of(n):
    cache = {0: 0, 1: 1}
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]


print(list(fibonacci_of(n) for n in range(15)))

