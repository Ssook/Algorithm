# 출처 : https://www.acmicpc.net/problem/1463
n = int(input())
d = [0, 0, 1, 1, 2]
answer = 0
# dp로 풀이
for i in range(5, n+1):
    targets = []
    if(i % 3 == 0):
        targets.append(d[i // 3]+1)
    if(i % 2 == 0):
        targets.append(d[i // 2]+1)
    targets.append(d[i-1]+1)
    d.append(min(targets))

print(d[n])
