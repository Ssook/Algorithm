# 출처 : https://www.acmicpc.net/problem/11048
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

d = [[0 for i in range(m+1)] for j in range(n+1)]
d[1][1] = graph[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        if(i == 1 and j == 1):
            continue
        d[i][j] = max(d[i-1][j]+graph[i-1][j-1], d[i][j-1]+graph[i-1][j-1])

print(d[n][m])
