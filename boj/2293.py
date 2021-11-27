# 출처 : https://www.acmicpc.net/problem/2293
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
d = [0 for _ in range(k+1)]
d[0] = 1


for coin in coins:
    for i in range(1, k+1):
        if(i-coin >= 0):
            d[i] += d[i-coin]

print(d[k])
