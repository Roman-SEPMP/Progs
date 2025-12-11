N = int(input())
tasks = []
time = []
ans = 0
for i in range(N):
    a, b = N, M = tuple(map(int, input().split()))
    tasks.append([a, b])

tasks = sorted(tasks, key = lambda x: x[1])

for n in range(len(tasks)):
    time.append(tasks[n][0])
    if sum(time) > tasks[n][1]:
        max_time = max(time)
        time.remove(max_time)
print(len(time))