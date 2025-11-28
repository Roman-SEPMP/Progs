N = int(input())
mines = []
ans = 1
for _ in range(N):
    a, b = map(int, input().split())
    mines.append([a, b])

s_mines = sorted(mines, key=lambda x: x[1])
det = s_mines[0][1]
for l, r in s_mines:
    if det < l:
        ans += 1
        det = r
print(ans)