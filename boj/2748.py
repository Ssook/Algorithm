# 출처 : https://www.acmicpc.net/problem/2748
n = int(input())
d = [0, 1, 1, 2]

for i in range(4, n+1):
    d.append(d[i-1]+d[i-2])

print(d[n])
