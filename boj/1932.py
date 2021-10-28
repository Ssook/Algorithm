# 출처 : https://www.acmicpc.net/problem/1932
n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[triangle[0][0]]]

for i in range(1, n):
    # 맨 왼쪽
    row = [dp[i-1][0]+triangle[i][0]]
    # 가운데
    for j in range(1, i):
        row.append(max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j]))
    # 맨 오른쪽
    row.append(dp[i-1][-1]+triangle[i][-1])

    dp.append(row)
print(max(dp[-1]))
