# 출처 : https://www.acmicpc.net/problem/11403
from collections import deque
global n
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visit = [0 for i in range(n)]


def bfs(start):
    global n
    visit = [0 for i in range(n)]
    queue = deque([start])
    # visit[start] = 1
    while(queue):
        cur = queue.popleft()

        for k in range(len(graph[cur])):
            if(graph[cur][k] == 1 and visit[k] == 0):
                queue.append(k)
                visit[k] = 1
    return visit


# 각 행마다 bfs수행
answer = []
for i in range(n):
    # for j in range(n):
    answer.append(bfs(i))


for a in answer:
    for k in a:
        print(k, end=' ')
    print('')
