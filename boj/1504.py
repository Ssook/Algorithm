# 출처 : https://www.acmicpc.net/problem/1504
import heapq
n, e = map(int, input().split())
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(e):
    s, e, c = map(int, input().split())
    graph[s-1][e-1] = c
    graph[e-1][s-1] = c

v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1


def dijkstra(start, end):
    INF = 99999999
    check = [0 for i in range(n)]
    distance = [INF for i in range(n)]

    distance[start] = 0
    queue = [(0, start)]
    while(queue):
        minDistance, cur = heapq.heappop(queue)
        if(check[cur] == 1):
            continue
        check[cur] = 1
        for i in range(len(graph[cur])):
            if(graph[cur][i] > 0 and distance[i] > distance[cur]+graph[cur][i]):
                distance[i] = distance[cur]+graph[cur][i]
                heapq.heappush(queue, (distance[i], i))

    return distance[end]


# s -> v1 -> v2 -> e와 s -> v2 -> v1 -> e 의 경로중 작은 값 출력
path1 = dijkstra(0, v1) + dijkstra(v1, v2) + dijkstra(v2, n-1)
path2 = dijkstra(0, v2) + dijkstra(v2, v1) + dijkstra(v1, n-1)

if(path1 < 99999999 or path2 < 99999999):
    print(min(path1, path2))
else:
    print(-1)
