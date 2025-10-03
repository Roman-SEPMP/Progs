n = int(input())
ans = [1]

#
primes = [i for i in range(n+1)]
primes[1] = 0
i = 2
ans = []
while i <= n:
    if primes[i] != 0:
        j = i + i
        while j <= n:
            primes[j] = 0
            j = j +i
    i += 1
primes = [i for i in primes if i != 0]
#
for i in primes:
    if n % i == 0:
        ans.append(i)
print(ans)
'''
for i in range(2, n+1):
    if n % i == 0:
        k = n // i
        ans.append(i)
        while k % i == 0:
            k = k // i
print(ans)
'''