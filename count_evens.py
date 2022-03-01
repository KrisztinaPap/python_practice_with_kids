def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)


count_even([3, 4, 5, 6, 7, 8, 9])

