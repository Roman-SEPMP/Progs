N = int(input())
pares = []
for _ in range(N):
    A, B = map(int, input().split())
    pares.append([A, B])
print(pares)