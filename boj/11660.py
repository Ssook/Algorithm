# 출처 : https://www.acmicpc.net/problem/11660

import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
# 각 행마다 누적합을 기록
for i in range(n):
    s = 0
    row = []
    for j in (map(int, sys.stdin.readline().split())):
        s += j
        row.append(s)
    graph.append(row)


for i in range(m):
    answer = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 1,1 2,3
    for x in range(x1-1, x2):
        if(y1 != 1):
            answer += graph[x][y2-1] - graph[x][y1-2]
        else:
            answer += graph[x][y2-1]
    print(answer)
