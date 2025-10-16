numbers = list(map(int, input().split()))
s = 0
c = 0
ans = numbers[0]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            c += 1
    if c > s:
        s = c
        ans = numbers[i]
    c = 0
print(ans)
            