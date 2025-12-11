import math

a = input().split()
f = True

for i in range(math.ceil(math.log2(len(a)))):
    if a[i] != "None":

        if a[i * 2 + 1] != "None":
            if int(a[i * 2 + 1]) > int(a[i]):
                f = False
                break

        if a[i * 2 + 2] != "None":
            if int(a[i * 2 + 2]) < int(a[i]):
                f = False
                break

if f:
    print("YES")
else:
    print("NO")