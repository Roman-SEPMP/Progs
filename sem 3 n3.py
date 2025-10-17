a = int(input())
b = int(input())
a1 = a
b1 = b
while a != 0 and b !=0:
    if a > b:
        a = a % b
    else:
        b = b % a
    d = (a + b)

ms = 0
for x in range(-d, d):
    if (d - a1 * x) % b1 == 0:
        y = (d - a1 * x) % b1
        s = x + y
        if ms <= s:
            ms = s
print(x, y, d)