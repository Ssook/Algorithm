# 출처 : https://www.acmicpc.net/problem/2252
from collections import deque
n, m = map(int, input().split())
graph = {}

# 인접리스트
for i in range(n):
    key = str(i)
    graph[key] = []

# 위상정렬
indegree = [0 for i in range(n)]
answer = []

for _ in range(m):
    s, e = map(int, input().split())
    key = str(s-1)
    graph[key].append(e-1)
    indegree[e-1] += 1

queue = deque([])
for i in range(len(indegree)):
    if(indegree[i] == 0):
        queue.append(i)

while(queue):
    cur = queue.popleft()
    answer.append(cur)
    key = str(cur)
    # 다음 노드 찾아서 indegree값 -1하고 0이 되었으면 큐에 푸쉬
    for node in graph[key]:
        indegree[node] -= 1
        if(indegree[node] == 0):
            queue.append(node)


for a in answer:
    print(a+1, end=' ')
