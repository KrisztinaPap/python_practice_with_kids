def first_last_6(lst):
    result = False
    if lst[0] == 6 or lst[-1] == 6:
        result = True
    print(result)


def first_last_6_2(lst):
    if lst[0] == 6 or lst[-1] == 6:
        return True
    else:
        return False


first_last_6([1, 2, 3, 4, 5, 6])
first_last_6_2([1, 2, 3, 4, 5, 6])
