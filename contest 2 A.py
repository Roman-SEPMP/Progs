text = input()
p = {')': '(', ']': '[', '}': '{'}
st = []
k = 0
for i in text:
    k += 1
    if i == '(' or i == '[' or i == '{':
        st.append(i)
    if i == ')' or i == ']' or i == '}':
        if len(st) == 0 or st[-1] != p[i]:
            ans = 'No'
            break
        else:
            st.pop()
if k == len(text) and len(st) == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)