# 출처 : https://www.acmicpc.net/problem/16194
n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)
INF = 987654321
d = [INF for _ in range(n+1)]
d[0] = 0
for i in range(0, n+1):
    target = []
    for j in range(0, i+1):
        target.append(cards[j]+d[i-j])
    d[i] = min(target)

print(d[n])
