# 출처 : https://www.acmicpc.net/problem/9461
t = int(input())
for _ in range(t):
    d = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    n = int(input())
    for i in range(11, n+1):
        # d[i] = d[i-1]+d[i-5] 점화식
        d.append(d[i-1]+d[i-5])
    print(d[n])
