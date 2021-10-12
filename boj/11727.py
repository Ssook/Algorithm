# 출처 : https://www.acmicpc.net/problem/11727
n = int(input())
d = [0, 1, 3, 5]
for i in range(4, n+1):
    d.append((d[i-1]+2*d[i-2]) % 10007)

print(d[n] % 10007)
