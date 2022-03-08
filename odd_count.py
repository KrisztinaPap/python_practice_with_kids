def odd_count(n):
    return sum(1 for x in range(1, n) if x % 2 == 1)


def odd_count(n):
    counter = 0
    for x in range(1, n):
        if x % 2 == 1:
            counter += 1
    return counter


def odd_count(n):
    counter = 0
    x = 1
    while x < n:
        if x % 2 == 1:
            counter += 1
    return counter


