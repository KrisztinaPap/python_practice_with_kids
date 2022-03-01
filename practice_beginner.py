count_even = 0
for x in range(1 ,10):
    if (x % 2 == 0):
        print(x)
        count_even+=1
print(f'There are {count_even} even numbers in this range.')