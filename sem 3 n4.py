size = int(input())
symb = input()
if size % 2 != 0:
    for i in range((size // 2) + 2):
        print(symb * i)
    for k in range((size // 2), 0, -1):
        print(symb * k)
else:
    for i in range((size // 2) + 1):
        print(symb * i)
    for k in range((size // 2), 0, -1):
        print(symb * k)