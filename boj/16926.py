# 출처 : https://www.acmicpc.net/problem/16926
import math
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

count = math.ceil(min(n, m)/2)

for d in range(r):
    for i in range(count):
        startValue = graph[i][i]
        # 위에거
        for col in range(i+1, m-i):
            graph[i][col-1] = graph[i][col]

        # 오른쪽거
        for row in range(i, n-i-1):
            graph[row][m-1-i] = graph[row+1][m-1-i]

        # 아래거
        for col in range(m-i-1, i, -1):
            graph[n-1-i][col] = graph[n-1-i][col-1]

        # 왼쪽거
        for row in range(n-i-1, i, -1):
            graph[row][i] = graph[row-1][i]

        graph[i+1][i] = startValue


for g in graph:
    for v in g:
        print(v, end=' ')
    print('')
