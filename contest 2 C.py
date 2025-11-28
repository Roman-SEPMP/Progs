def dnksort(dnk, n):
    c = 0
    for i in range(n):
        for j in range(i, n):
            if dnk[i] > dnk[j]:
                c += 1
    return(dnk, c)

K = int(input())
for j in range(K):
    tests = []
    n, m = tuple(map(int, input().split()))
    for i in range(m):
        s=input()
        tests.append((dnksort(s, n)))
        tests = sorted(tests, key = lambda x: x[1])
    for k in range(len(tests)):
        print(tests[k][0])
    if j < K-1:
        print(' ')
