# 출처 : https://www.acmicpc.net/problem/1260

from collections import deque
n, m, v = map(int, input().split())

visit = [0 for i in range(n)]

graph = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

dfsList = []
# dfsList.append(str(v))


def dfs(curNode):
    visit[curNode] = 1
    dfsList.append(str(curNode+1))
    for i in range(n):
        if(visit[i] == 0 and graph[curNode][i] == 1):
            dfs(i)


dfs(v-1)
print(" ".join(dfsList))
# bfs
visit = [0 for i in range(n)]
queueRoad = []
queue = deque([v-1])
while(queue):
    curNode = queue.popleft()
    queueRoad.append(str(curNode+1))
    visit[curNode] = 1
    for i in range(n):
        if(graph[curNode][i] == 1 and visit[i] == 0):
            visit[i] = 1
            queue.append(i)

print(" ".join(queueRoad))
