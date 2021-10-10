# 출처 : https://www.acmicpc.net/problem/1697
from collections import deque
n, k = map(int, input().split())
visit = [0 for i in range(100001)]
queue = deque([n])
costs = deque([0])
answer = []
while(queue):
    cur = queue.popleft()
    cost = costs.popleft()

    if(cur == k):
        answer.append(cost)
    possible = []
    if(cur-1 >= 0):
        possible.append(cur-1)
    if(cur+1 <= 100000):
        possible.append(cur+1)
    if(cur*2 <= 100000):
        possible.append(cur*2)
    for p in possible:
        if(visit[p] == 0):
            visit[p] = 1
            queue.append(p)
            costs.append(cost+1)

print(min(answer))
