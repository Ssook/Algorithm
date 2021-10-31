# 출처 : https://www.acmicpc.net/problem/11779
import sys
import heapq
import copy
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[-1 for i in range(n+1)] for j in range(n+1)]

graphDict = {}
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if(graph[a][b] == -1):
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

start, end = map(int, sys.stdin.readline().split())
INF = int(1e9)+1

check = [0 for i in range(n+1)]
distance = [INF for i in range(n+1)]

distance[start] = 0
queue = [(0, start)]
paths = [[] for i in range(n+1)]
answer = ''
while(queue):
    cost, cur = heapq.heappop(queue)
    if(distance[cur] < cost):
        continue
    paths[cur].append(cur)

    if(cur == end):
        answer = paths[cur]
    for i in range(len(graph[cur])):
        if(graph[cur][i] >= 0 and distance[i] > cost+graph[cur][i]):
            distance[i] = cost+graph[cur][i]
            heapq.heappush(queue, ((cost+graph[cur][i], i)))
            paths[i] = copy.deepcopy(paths[cur])

print(distance[end])
print(len(answer))
for a in answer:
    print(a, end=' ')
