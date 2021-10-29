# 출처 : https://www.acmicpc.net/problem/12865
n, k = map(int, input().split())

items = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

items.sort(key=lambda x: x[0])

d = [[0 for i in range(k+1)] for j in range(n+1)]
# dp
for i in range(n+1):
    for j in range(k+1):
        if(i != 0 and j != 0):
            # 이번 아이템이 들고 있을 수 있는 무게 보다 작은 경우
            if(items[i][0] <= j):
                # 이번거를 선택하면 전단계에서 현재 선택한 아이템의 무게를 뺀 dp값과 전단계의 현재 무게에서 들 수 있는 값중 큰값을 선택
                d[i][j] = max(d[i-1][j-items[i][0]]+items[i][1], d[i-1][j])
            elif(items[i][0] > j):
                # 들 수 없는 아이템이라면 전단계랑 동일한 값
                d[i][j] = d[i-1][j]

print(d[-1][-1])
