# 출처 : https://www.acmicpc.net/problem/1766

# 위상정렬 풀이
import heapq
answer = []
n, m = map(int, input().split())

graph = {}
for i in range(n):
    graph[str(i)] = []
indegree = [0 for _ in range(n)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[str(s-1)].append(e-1)
    indegree[e-1] += 1

queue = []
for i in range(len(indegree)):
    if(indegree[i] == 0):
        queue.append(i)

while(queue):
    cur = heapq.heappop(queue)
    answer.append(cur)
    for node in graph[str(cur)]:
        indegree[node] -= 1
        if(indegree[node] == 0):
            heapq.heappush(queue, node)

for a in answer:
    print(a+1, end=' ')
