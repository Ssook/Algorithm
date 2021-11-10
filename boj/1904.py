# 출처 : https://www.acmicpc.net/problem/1904
n = int(input())

d = [0, 1, 2]

for i in range(3, n+1):
    d.append((d[i-1]+d[i-2]) % 15746)

print(d[n] % 15746)
