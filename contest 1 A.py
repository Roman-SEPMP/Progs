N, M = tuple(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
F = [[0] * (M + 1) for _ in range(N +1)]

for i in range(1, N + 1):
    for m in range(1, M + 1):
        if m >= x[i - 1]:
            F[i][m] = max(F[i - 1][m], F[i - 1][m - x[i - 1]] + y[i - 1])
        else:
            F[i][m] = F[i - 1][m]
print(F[-1][-1])