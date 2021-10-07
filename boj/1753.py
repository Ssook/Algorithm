# 출처 : https://www.acmicpc.net/problem/1753
import heapq
n, m = map(int, input().split())
INF = 100000000
graph = [{} for i in range(n)]
check = [0 for i in range(n)]
distance = [INF for i in range(n)]

start = int(input())-1

# 인접 리스트
for i in range(m):
    a, b, d = map(int, input().split())
    key = b-1
    if(key in graph[a-1]):
        graph[a-1][key] = min(graph[a-1][key], d)
    else:
        graph[a-1][key] = d

# distance 는 start부터 n까지의 최단 거리
distance[start] = 0
queue = [(0, start)]
# 다익스트라, 시간복잡도 때문에 힙을 사용하여 가장 가까운 노드 구함
# d[to]= d[from]+cost
while(queue):
    minDistance, nowIndex = heapq.heappop(queue)
    if(check[nowIndex] == 1):
        continue
    check[nowIndex] = 1
    # 현재 정점에서 갈 수 있는 정점중 더 작은 비용으로 갈 수 있으면 distance 갱신해주고 큐에 삽입
    for key in graph[nowIndex]:
        index = key
        value = graph[nowIndex][key]
        if(distance[nowIndex]+value < distance[index]):
            distance[index] = distance[nowIndex]+value
            heapq.heappush(queue, (distance[index], index))

for d in distance:
    if(d != INF):
        print(d)
    else:
        print('INF')
