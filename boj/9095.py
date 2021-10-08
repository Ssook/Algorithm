# 출처 : https://www.acmicpc.net/problem/9095
t = int(input())
d = [0 for i in range(13)]
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 13):
    d[i] = d[i-1]+d[i-2]+d[i-3]

for k in range(t):

    n = int(input())
    print(d[n])
