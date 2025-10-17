numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            break
    else:
        print(numbers[i])