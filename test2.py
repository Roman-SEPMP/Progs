num = int(input())
c = int(input())
num10 = 0
for j in range(len(str(num))):
    k = len(str(num)) - j - 1
    num10 += int(str(num)[j]) * (c ** k)
print(num10)