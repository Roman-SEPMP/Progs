s = input().split()
words = {}
only = []
only_l = []
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

sorted_words = quick_sort(l_words)

SortedWords = [pair for pair in sorted_words if len(pair[1]) > 1]
only = [a for a in sorted_words if len(a[1]) == 1]
only_l = [pair[1][0] for pair in only]
only_l.sort()
if len(SortedWords) != 0:
    print(" ".join([a for pair in SortedWords for a in pair[1]]),  ' '.join(only_l))
else: 
    print(' '.join(only_l))
'''
for i in only:
    only[i][1].sort
print(" ".join([a for pair in quick_sort(sorted_words) for a in pair[1]]) + " ".join([a for pair in quick_sort(only) for a in pair[1]]))

#print(" ".join([a for pair in quick_sort(l_words) for a in pair[1]]))
'''