# число вводится в 1-й строке, а набор букв во второй
c = int(input())
M = input()

ans = ''
while len(M) >= c:
    for i in range(c):
        ans += M[c-i-1]
    M = M[c: ]
print(ans)
