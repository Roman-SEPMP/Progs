n, m = tuple(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(n)]
INF = 1001
F = [[0] * m for _ in range(n)] # Заполняем F в верном формате
for y in range(n):
    for x in range(m):
        F[y][x] = [-INF, -INF, -INF]

F[0][0]= [D[0][0], D[0][0], D[0][0]] # Заполняем начальные условия
if n > 1:
    F[1][0] = [D[1][0] + D[0][0], D[1][0] + D[0][0], D[1][0] + D[0][0]]
if m > 1:
    F[0][1] = [D[0][1] + D[0][0], D[0][1] + D[0][0], D[0][1] + D[0][0]]

for y in range(1, n): # Сам алгоритм
    for x in range(1, m):
        Fy = max(F[y-1][x][1], F[y-1][x][2]) + D[y][x]
        Fd = max(F[y-1][x-1][0], F[y-1][x-1][2]) + D[y][x]
        Fx = max(F[y][x-1][0], F[y][x-1][1]) + D[y][x]
        F[y][x] = [Fy, Fd, Fx]
print(max(F[-1][-1][0], F[-1][-1][1], F[-1][-1][2]))