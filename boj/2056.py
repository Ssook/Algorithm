# 출처 : https://www.acmicpc.net/problem/2056

# 위상 정렬 + dp
from collections import deque

n = int(input())
graphDict = {}
for i in range(n):
    graphDict[str(i)] = []
times = [0 for i in range(n)]
indegree = [0 for i in range(n)]
answer = 0
for i in range(n):
    l = list(map(int, input().split()))
    times[i] = l[0]
    indegree[i] += l[1]
    for j in range(l[1]):
        graphDict[str(l[2+j]-1)].append(i)

dp = [0 for i in range(n)]
queue = deque([])
# 인디그리값이 0인거부터 탐색 시작
for i in range(len(indegree)):
    if(indegree[i] == 0):
        queue.append(i)
        dp[i] = times[i]


while(queue):
    cur = queue.popleft()
    for node in graphDict[str(cur)]:
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)
        # 탐색할 노드의 작업 완료시간은 현재 노드에 온시간 + 탐색할 노드의 작업 시간
        dp[node] = max(dp[node], dp[cur]+times[node])
print(max(dp))
