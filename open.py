def fib(n):
    numbers = [0] * n
    numbers[0] = 1
    numbers[1] = 1

    for i in range(2, n):
        numbers[i] = numbers[i - 1] + numbers[i -2]
    return numbers[n -1]
print(fib(10))
