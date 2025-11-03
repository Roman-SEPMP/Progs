N = int(input()) + 1
K = N
F = [[0] * N for _ in range(K)]
for i in range(K):
    F[i][0] = 1
for k in range(1, K):
    for n in range(1, N):
            F[k][n] = F[k-1][n] + F[k//2][n-k]
print(F[-1][-1])


            