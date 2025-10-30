n, m = tuple(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(n)]
D[1][2] = [3, -1, 5]
print(D)
