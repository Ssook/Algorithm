# 출처 : https://www.acmicpc.net/problem/11725
from collections import deque
n = int(input())

graph = {}
parent = [0 for i in range(n+1)]

# 이차원배열로 하면 시간 초과
for i in range(n-1):
    a, b = map(int, input().split())
    key1 = str(a)
    key2 = str(b)
    if(key1 in graph):
        graph[str(a)].append(b)
    else:
        graph[str(a)] = [b]

    if(key2 in graph):
        graph[str(b)].append(a)
    else:
        graph[str(b)] = [a]

queue = deque([1])
visit = [0 for i in range(n+1)]
visit[1] = 1
# 1번부터 시작해서 부모 노드를 찾아준다.
while(queue):
    cur = queue.popleft()
    for i in graph[str(cur)]:
        if(visit[i] == 0):
            parent[i] = cur
            queue.append(i)
            visit[i] = 1


for p in parent[2:]:
    print(p)
