# 출처 : https://www.acmicpc.net/problem/13699
n = int(input())
t = [0 for i in range(n+1)]
t[0] = 1

for i in range(1, n+1):
    s = 0
    a = 0

    for j in range(i):
        a += t[j]*t[i-j-1]
    t[i] = a

print(t[n])
