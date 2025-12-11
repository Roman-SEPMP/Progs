
n, q = tuple(map(int, input().split()))
S = input()
oper = []
for _ in range(q):
    l, r, k = map(int, input().split())
    srez = S[l:r]
    if k == 1:
        srez.sort()
    if k == 0:
        srez.sort(reverse = True)
'''
    if k == 1:
        S = ''.join(sorted(S[l: r]))
    else:
        S = ''.join(sorted(S[l: r]), reverse = True)
'''
print(S)
