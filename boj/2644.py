# 출처 : https://www.acmicpc.net/problem/2644
from collections import deque
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

queue = deque([p1])
counts = deque([0])
visit = [0 for i in range(n+1)]
visit[p1] = 1
answer = -1
while(queue):
    cur = queue.popleft()
    count = counts.popleft()
    if(cur == p2):
        answer = count
        break
    for i in range(1, n+1):
        if(graph[cur][i] == 1 and visit[i] == 0):
            queue.append(i)
            counts.append(count+1)
            visit[i] = 1

print(answer)
