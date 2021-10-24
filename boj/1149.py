# 출처 : https://www.acmicpc.net/problem/1149
n = int(input())
costs = [[0, 0, 0]]
for i in range(n):
    r, g, b = map(int, input().split())
    costs.append([r, g, b])

d = [[0 for i in range(3)] for j in range(n+1)]

# d[i][j]는 i번째 차례에 j(rgb)번째 색을 칠했을 때 최소 비용
for i in range(1, n+1):
    for j in range(3):
        prevCost = d[i-1]
        minCost = 99999999999
        for k in range(3):
            if(j != k):
                minCost = min(prevCost[k], minCost)
        d[i][j] = minCost+costs[i][j]


print(min(d[n]))
