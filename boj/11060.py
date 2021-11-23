# 출처 : https://www.acmicpc.net/problem/11060
from collections import deque
n = int(input())
Ai = list(map(int, input().split()))
Ai.insert(0, 0)
queue = deque([1])
count = deque([0])

visit = [0 for i in range(n+1)]
answer = -1
while(queue):
    cur = queue.popleft()
    c = count.popleft()
    if(cur == n):
        answer = c
        break
    # 1부터 현재칸에 쓰여져있는 수만큼
    for i in range(1, Ai[cur]+1):
        if(cur+i <= n and visit[cur+i] == 0):
            queue.append(cur+i)
            count.append(c+1)
            visit[cur+i] = 1


print(answer)
