# 출처 : https://www.acmicpc.net/problem/12851
from collections import deque
n, k = map(int, input().split())

counts = deque([0])
queue = deque([n])
visit = [999999 for i in range(100001)]
visit[n] = 0
answer = []
while(queue):
    cur = queue.popleft()
    count = counts.popleft()
    if(answer):
        if count > answer[0]:
            continue
    if(cur == k):
        answer.append(count)
        continue
    # x-1
    if(cur-1 >= 0 and visit[cur-1] >= count+1):
        queue.append(cur-1)
        counts.append(count+1)
        visit[cur-1] = count+1
    # x+1
    if(cur+1 <= 100000 and visit[cur+1] >= count+1):
        queue.append(cur+1)
        counts.append(count+1)
        visit[cur+1] = count+1
    # x*2
    if(cur*2 <= 100000 and visit[cur*2] >= count+1):
        queue.append(cur*2)
        counts.append(count+1)
        visit[cur*2] = count+1

print(answer[0])
print(len(answer))
