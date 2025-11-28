a = [6, 9, 3, -2, 0, 1, 48]
N = len(a)
for i in range(N - 1):
    for j in range(N - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)