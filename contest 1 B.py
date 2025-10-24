a, b = map(int, input().split())
x = 0
while (a + x) % b != 0 or (b + x) % a != 0:
    x += 1
print(x)