n, q = map(int, input().split())
S = list(input())
for _ in range(q):
    l, r, k = map(int, input().split())
    l -= 1
    srez = S[l:r]
    if k == 1:
        srez.sort()
    else:
        srez.sort(reverse=True)
    S[l:r] = srez
print("".join(S))
'''
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
print(S)

    if k == 1:
        S = ''.join(sorted(S[l: r]))
    else:
        S = ''.join(sorted(S[l: r]), reverse = True)
'''

