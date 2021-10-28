# 출처 : https://www.acmicpc.net/problem/1238
import heapq

# 그래프 그리기
n, m, x = map(int, input().split())
x -= 1
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    s, e, t = map(int, input().split())
    graph[s-1][e-1] = t

# s -> e 로가는 최단 경로의 가중치


def daikstra(start, end):
    distance = [999999 for i in range(n)]
    check = [0 for i in range(n)]
    queue = [(0, start)]
    distance[start] = 0
    while(queue):
        minDistance, cur = heapq.heappop(queue)
        if(check[cur] == 1):
            continue
        for i in range(len(graph[cur])):
            if(graph[cur][i] > 0):
                if(distance[i] > minDistance+graph[cur][i]):
                    distance[i] = minDistance+graph[cur][i]
                    heapq.heappush(queue, (distance[i], i))

    return distance[end]


answer = [0 for i in range(n)]
for i in range(n):
    # n->x + x->n
    answer[i] = daikstra(i, x) + daikstra(x, i)

print(max(answer))
