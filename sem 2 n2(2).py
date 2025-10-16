n = int(input())
ans = []
for i in range(2, n+1):
    if n % i == 0:
        for j in range(2, i+1):
            if i % j == 0:
                break
            ans.append(i)
# черновик