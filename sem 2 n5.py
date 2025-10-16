numbers = list(map(int, input().split()))
a = numbers[-1]
print(a)
numbers.pop(-1)
numbers.insert(0, int(a))
print(numbers)