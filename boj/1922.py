# 출처 : https://www.acmicpc.net/problem/1922
# mst
import sys
import heapq
n = int(sys.stdin.readline())
graph = [[0 for i in range(n)] for j in range(n)]
m = int(sys.stdin.readline())
check = [0 for i in range(n)]
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = cost
    graph[b-1][a-1] = cost

answer = 0
queue = [(0, 0)]
# 가중치가 작은 것부터 탐색
while(queue):
    cost, cur = heapq.heappop(queue)
    # 이미 탐색했다면 스킵
    if(check[cur]):
        continue
    answer += cost
    check[cur] = 1
    for i in range(len(graph[cur])):
        if(graph[cur][i] > 0):
            heapq.heappush(queue, (graph[cur][i], i))

print(answer)
