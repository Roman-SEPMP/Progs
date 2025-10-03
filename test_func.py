n = int(input())
ans = []
for i in range(1, n+1):
    for j in range(2, i+1):
        if i % j == 0:
            b = 0
            break
        else:
            b = 1
        print(b)
    
