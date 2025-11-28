N = int(input())
mines = []

for _ in range(N):
    a, b = map(int, input().split())
    mines.append([a, b])
for i in range(N):
        for j in range(0, N - i - 1):
            if mines[j][1] > mines[j + 1][1]:
                mines[j], mines[j + 1] = mines[j + 1], mines[j]
det = [mines[0][1]]
k = 1
for i in range(N):
    if mines[i][0] <= det[k-1] <= mines[i][1]:
        continue
    else:
        k += 1
        det.append(mines[i][1])
print(k)