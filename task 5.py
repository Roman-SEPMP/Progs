# task 5
N = input()
b = int(input())
c = int(input())
sum10 = 0
for i in range(len(N)):
    k = len(N) - i - 1
    sum10 += int(N[i]) * (b ** k)

if c < 10:
    ans= ''
    while sum10 // c > 0:
        a = sum10 % c
        sum10 = sum10 // c
        ans += str(a)
    ans += str(sum10 % c)
    #ans += str(a)
    print(ans[: :-1])
else:
    print(sum10)