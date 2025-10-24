m, n = tuple(map(int, input().split()))
f = 0
s = 0
while m % 2 != 0 and n % 2 != 0:
    m = m // 2
    n = n // 2
    s += 4 ** f
    f += 1
print(s)