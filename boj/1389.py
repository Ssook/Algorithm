# # 출처 : https://www.acmicpc.net/problem/1389
# from collections import deque
# n, m = map(int, input().split())
# visits = []
# # 그래프 그리기
# graph = [[0 for i in range(n)] for j in range(n)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a-1][b-1] = 1
#     graph[b-1][a-1] = 1

# # 모든 정점에 대해서 bfs 수행
# for _ in range(n):
#     visit = [-1 for i in range(n)]
#     queue = deque([_])
#     visit[_] = 0
#     check = deque([0])
#     while(queue):
#         cur = queue.popleft()
#         count = check.popleft()

#         for i in range(len(graph[cur])):
#             if(visit[i] == -1 and graph[cur][i] > 0):
#                 queue.append(i)
#                 check.append(count+1)
#                 # visit에 몇번 째 방문인지 기록
#                 visit[i] = count+1

#     visits.append(sum(visit))

# print(1+visits.index(min(visits)))

# 플로이드
n, m = map(int, input().split())
visits = []
INF = 987654321
# 그래프 그리기
graph = [[INF for i in range(n)] for j in range(n)]
for i in range(n):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


maxV = 999999
maxIdx = 99999
for i in range(n-1, -1, -1):
    if sum(graph[i]) <= maxV:
        maxV = sum(graph[i])
        maxIdx = i

print(maxIdx+1)
