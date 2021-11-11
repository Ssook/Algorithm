# 출처 : https://www.acmicpc.net/problem/2096
# 메모리 초과 주의
n = int(input())
dMax = [0, 0, 0]
dMin = [0, 0, 0]
tMax = [0, 0, 0]
tMin = [0, 0, 0]
for i in range(n):
    a, b, c = map(int, input().split())
    tMax[0] = max(dMax[0], dMax[1])+a
    tMax[1] = max(dMax[0], dMax[1], dMax[2])+b
    tMax[2] = max(dMax[1], dMax[2])+c
    for j in range(3):
        dMax[j] = tMax[j]

    tMin[0] = min(dMin[0], dMin[1])+a
    tMin[1] = min(dMin[0], dMin[1], dMin[2])+b
    tMin[2] = min(dMin[1], dMin[2])+c
    for j in range(3):
        dMin[j] = tMin[j]
print(max(dMax), min(dMin))
