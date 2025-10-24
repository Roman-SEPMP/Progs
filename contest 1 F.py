n, k = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    j = i ^ k
    if j <= (2 ** n):
        sum = numbers[j] + numbers[i]
    else:
        continue
    if sum > ans:
        ans = sum
print(ans)