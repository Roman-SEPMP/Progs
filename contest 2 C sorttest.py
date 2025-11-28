def dnksort(dnk):
    c = 0
    for i in range(len(dnk)):
        for j in range(i, len(dnk)):
            if dnk[i] > dnk[j]:
                c += 1
    return(dnk, c)
print(dnksort(input()))
'''
tests = []
n, m = tuple(map(int, input().split()))
for i in range(m):
    s=input()
#        podscet_c=c
    tests.append((dnksort(s)))
print(tests)
'''