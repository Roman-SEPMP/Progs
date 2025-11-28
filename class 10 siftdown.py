a = [6, 9, 3, -2, 0, 1, 48]
N = len(a)


def siftDown(a, i):
    if i > len(a)//2 - 1:
        return
    
    if 2 * i + 2 < len(a)//2 - 1:
        if a[i] < a[2 * i + 1]:
            a[i], a[2 * i + 1]

    maxChild = max(a[2*i + 1], a[2 * i + 2])
    maxChildindex = a.index(maxChild)
    if a[i] > maxChild:
        return
    else:
        a[i], a[maxChildindex] = a[maxChildindex], a[i]
        siftDown(a, maxChildindex)

# делаем кучу
for i in range(N//2, -1, -1):
    siftDown(a, i)
print(a)

# сортируем
for i in range(N, 0, -1):
    a[0], a[i - 1] = a[i - 1], a[0]
    siftDown(a[:i - 1], 0)