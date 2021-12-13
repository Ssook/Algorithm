# 출처 : https://www.acmicpc.net/problem/2302
n = int(input())

# dp 배열
d = [0 for i in range(n+1)]
d[0] = 1
d[1] = 1
d[2] = 2

# 경우의 수 계산
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]
m = int(input())
vip = [int(input()) for _ in range(m)]

breakPoint = 0
answer = 1

# 고정된 점을 기준으로 각 이어져있는 수의 경우의 수를 곱
for v in vip:
    answer *= d[v-breakPoint-1]
    breakPoint = v

# 마지막 고정점 이후의 경우의 수 
answer *= d[n-breakPoint]

print(answer)
