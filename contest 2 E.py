s = input().split()
words = {}
for word in s:
    s_word = ''.join(sorted(word))
    if s_word in words:
        words[s_word].append(word)
    else:
        words[s_word] = [word]
for i in words:
    words[i].sort()

l_words = list(words.items())


def quick_sort(arr):
    if len(arr) <= 1:
        return arr 

    pivot = arr[len(arr) // 2] 

    left = [arr[i] for i in range(len(arr)) if len(arr[i][1]) < len(pivot[1])]
    middle = [arr[i] for i in range(len(arr)) if len(arr[i][1]) == len(pivot[1])]   
    right = [arr[i] for i in range(len(arr)) if len(arr[i][1]) > len(pivot[1])]     

    return quick_sort(right) + middle + quick_sort(left)


print(" ".join([a for pair in quick_sort(l_words) for a in pair[1]]))


