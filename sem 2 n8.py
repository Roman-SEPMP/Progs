count = int(input())
numbers = list(map(int, input().split()))
m = count // 2
c = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] > numbers[j]:
            c += 1
    if c == m:
        print(numbers[i])
    c = 0