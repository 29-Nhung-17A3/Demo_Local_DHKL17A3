def day_so(n):
    numbers = list(range(1, n + 1))

    numbers.reverse()

    for number in numbers:
        if number % 2 != 0:
            print(number)

day_so(10)