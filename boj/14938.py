# 출처 : https://www.acmicpc.net/problem/14938
import heapq
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items.insert(0, 0)
graph = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

answer = []
# 모든 정점에 대해서 다익스트라 수행
for i in range(1, n+1):
    start = i
    distance = [9999999 for i in range(n+1)]
    check = [0 for i in range(n+1)]
    queue = [(0, start)]
    while(queue):
        cost, cur = heapq.heappop(queue)

        if(check[cur] == 1):
            continue

        for j in range(1, n+1):
            if(graph[cur][j] > 0 and check[j] == 0 and distance[j] > cost+graph[cur][j]):
                distance[j] = cost+graph[cur][j]
                heapq.heappush(queue, (cost+graph[cur][j], j))

    total = items[start]
    for j in range(1, n+1):
        # 시작점이랑 같은 노드는 제외
        if(j == start):
            continue
        if(distance[j] <= m):
            total += items[j]
    answer.append(total)

print(max(answer))
