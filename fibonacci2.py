class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(
                f'Positive integer expected, got "{n}"'
            )

        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_num = self(n - 1) + self(n - 2)
            self.cache.append(fib_num)
        return self.cache[n]


fibonacci = Fibonacci()
print(fibonacci(15))
print([fibonacci(n) for n in range(12)])

