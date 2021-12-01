# 출처 : https://www.acmicpc.net/problem/5567
from collections import deque
n = int(input())
m = int(input())

graph = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

answer = 0

queue = deque([1])
visit = [0 for i in range(n+1)]
visit[1] = 1
distance = deque([0])

while(queue):
    cur = queue.popleft()
    d = distance.popleft()

    if(d == 3):
        break
    for i in range(1, n+1):
        if(graph[cur][i] == 1 and visit[i] == 0 and d < 2):
            queue.append(i)
            distance.append(d+1)
            visit[i] = 1

for v in visit:
    if(v == 1):
        answer += 1

print(answer - 1)
