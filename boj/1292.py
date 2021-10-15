# 출처 : https://www.acmicpc.net/problem/1292
start, end = map(int, input().split())

d = [0]
n = 1
while(len(d) <= 1000):
    for i in range(n):
        d.append(n)
    n += 1

print(sum(d[start:end+1]))
