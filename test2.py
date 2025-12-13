a, b = input().split()
a = int(a)
b = int(b)
a1 = a
b1 = b

# исправление №1 — правильный алгоритм Евклида
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
d = a + b   # одно из чисел стало 0 → сумма = НОД

best_x = None
best_y = None
best_s = None

# оставляем твою идею перебора, только исправляем ошибки
for x in range(-d*5, d*5 + 1):
    # проверяем, существует ли целый y
    if (d - a1 * x) % b1 == 0:
        y = (d - a1 * x) // b1

        s = abs(x) + abs(y)

        if (best_s is None) or (s < best_s) or (s == best_s and x < best_x):
            best_s = s
            best_x = x
            best_y = y

print(best_x, best_y, d)