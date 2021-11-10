# 출처 : https://www.acmicpc.net/problem/2193
n = int(input())
d = [[0 for i in range(2)] for j in range(n+1)]
# d[i][j] == i자리수의 끝자리가 j인 갯수
d[1][0] = 0
d[1][1] = 1

for i in range(2, n+1):
    d[i][0] += d[i-1][0]  # 전단계에서 0에다가 0을 붙이는 경우
    d[i][0] += d[i-1][1]  # 전단계에서 0에다가 1을 붙이는 경우
    d[i][1] += d[i-1][0]  # 전단계에서 1에다가 0을 붙이는 경우

print(d[n][0]+d[n][1])
