# task 6

f = open('input.txt')
number = f.readline()
number = list(map(int, number.split()))
sign = f.readline(2) #знак
c = int(f.readline(3)) #система счисления

number10 = []

for num in number:
    num10 = 0
    for j in range(len(str(num))):
        k = len(str(num)) - j - 1
        num10 += int(str(num)[j]) * (c ** k)
    number10.append(num10)

if sign == '+\n':
    res10 = sum(number10)

elif sign == '-\n':
    res10 = sum(number10)*(-1)

elif sign == '*\n':
    res10 = 1
    for i in number10:
        res10 *= i

ans =''
while res10 // c > 0:
    a = res10 % c
    ans += str(a)
    res10 = res10 // c
ans += str(res10 % c)

print(ans[ : :-1])
