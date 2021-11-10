# 출처 : https://www.acmicpc.net/problem/1956
v, e = map(int, input().split())
INF = 9999999
graph = [[INF for i in range(v+1)] for j in range(v+1)]

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# 플로이드
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if(graph[i][j] > graph[i][k]+graph[k][j]):
                graph[i][j] = graph[i][k]+graph[k][j]

answer = INF

# i==j이면서 INF가 아니면 자기 자신으로 오는 경로가 있다는 의미
for i in range(1, v+1):
    for j in range(1, v+1):
        if(i == j and graph[i][j] != INF):
            answer = min(answer, graph[i][j])
if(answer == INF):
    print(-1)
else:
    print(answer)
