n, m = tuple(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(n)]

F = [[0] * m for _ in range(n)]
F[0][0] = D[0][0]
F[1][0] = D[1][0]
F[0][1] = D[0][1]
INF = 1e10

for x in range(1, m-1):
    for y in range(1, n-1):
        F[x][y] = max(F[x-1][y], F[x][y-1], F[x-1][y-1]) + D[x][y]
        if F[x][y] == F[x-1][y] + D[x][y] and x <= n-2:
            F[x+1][y] = -INF
        elif F[x][y] == F[x][y-1] + D[x][y] and y <= m-2:
            F[x][y+1] = -INF
        elif F[x][y] == F[x-1][y-1] + D[x][y] and x <= n-2 and y <= m-2:
            F[x+1][y+1] = -INF
print(F)
print(F[-1][-1])