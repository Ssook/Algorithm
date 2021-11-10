# 출처 : https://www.acmicpc.net/problem/11404
n = int(input())
m = int(input())
INF = 19999999
graph = [[INF for i in range(n+1)] for j in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)

# 플로이드워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if(graph[i][j] == INF):
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print('')
