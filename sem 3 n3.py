a, b = map(int, input().split())
a1 = a
b1 = b
while a != 0 and b !=0:
    if a > b:
        a = a % b
    else:
        b = b % a
    d = (a + b)

ms = None
mx = None
my = None
for x in range(-d*5, d*5 + 1):
    if (d - a1 * x) % b1 == 0:
        y = (d - a1 * x) // b1
        s = abs(x) + abs(y)
        if (ms is None) or (s < ms):
            ms = s
            mx = x
            my = y
print(mx, my, d)