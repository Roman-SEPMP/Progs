k = int(input())
rang = []
for i in range(1,k+1):
    if k % i == 0:
        rang.append(k // 1)
    continue
print(rang)