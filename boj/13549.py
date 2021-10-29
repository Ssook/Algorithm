# 출처 : https://www.acmicpc.net/problem/13549
from collections import deque

n, k = map(int, input().split())
visit = [0 for i in range(100001)]

queue = deque([n])
costs = deque([0])
visit[n] = 1
answer = 0
while(queue):
    cur = queue.popleft()
    cost = costs.popleft()

    if(cur == k):
        answer = cost
        break
    mul = cur*2
    # 두배인 수들 다 넣어줌
    while(True):
        # print(mul)
        if(mul == 0 or mul > 100001):
            break
        if(visit[mul] == 0):
            visit[mul] = 1
            costs.append(cost)
            queue.append(mul)
        mul *= 2

    # +1, -1 처리
    for m in [cur+1, cur-1]:
        if(m >= 0 and m <= 100000 and visit[m] == 0):
            visit[m] = 1
            queue.append(m)
            costs.append(cost+1)

print(answer)
