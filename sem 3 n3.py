a = int(input())
b = int(input())
while a != 0 and b !=0:
    if a > b:
        a = a % b
    else:
        b = b
    d = (a + b)
print(d)

ms = 0
for x in range(-d, d):
    if (d - a * x) % b == 0:
        y = (d - a * x) % b
        s = x + y
        if ms <= s:
            ms = s
print(x, y, d)