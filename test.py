f = open('input.txt')
number = f.readline()
number = list(map(int, number.split()))
sign = f.readline(2) #знак
c = int(f.readline(3)) #система счисления
print(number)

number10 = []

for num in number:
    num10 = 0
    for j in range(len(str(num))):
        k = len(str(num)) - j - 1
        num10 += int(str(num)[j]) * (c ** k)
    number10.append(num10)
print(number10)

