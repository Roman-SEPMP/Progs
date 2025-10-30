n, m = tuple(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(n)]

INF = 1e10
F = [[-INF] * m for _ in range(n)]
F[0][0] = D[0][0]
if n > 1:
    F[1][0] = D[1][0] + D[0][0]
if m > 1:
    F[0][1] = D[0][1] + D[0][0]

for y in range(1, n):
    for x in range(1, m):
        F[y][x] = max(F[y-1][x], F[y][x-1], F[y-1][x-1]) + D[y][x]
        if y+1 < n and F[y][x] == F[y-1][x] + D[y][x]:
            F[y+1][x] = -INF
        if x+1 < m and F[y][x] == F[y][x-1] + D[y][x]:
            F[y][x+1] = -INF
        if x+1 < m and y+1 < n and F[y][x] == F[y-1][x-1] + D[y][x]:
            F[y+1][x+1] = -INF
print(F[-1][-1])