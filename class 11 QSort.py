a =[6, 9, 3, -2, 0, 1, 48]
N = len(a)

def quicksort(a):
    if len(a) <= 1:
        return a
    base = a[len(a)//2]
    left = []
    right = []
    center = []
    for i in range(len(a)):
        if a[i] < base:
            left.append(a[i])
        if a[i] > base:
            right.append(a[i])
        else: 
            center.append(a[i])
        return quicksort(left) + center + quicksort(right)
print(quicksort(a))