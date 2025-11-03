N = int(input()) + 1
K = N
c = 0
F = [[0] * N for _ in range(K)]
for i in range(K):
    F[i][0] = 1
for k in range(1, K):
    for n in range(1, N - c):
        F[k][n] = F[k-1][n] + F[k//2][n-k]
    F[k][-1] = F[k-1][-1] + F[k//2][N - 1 - k]
    c += 2
print(F[-1][-1])
