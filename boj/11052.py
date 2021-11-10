# 출처 : https://www.acmicpc.net/problem/11052
n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)

d = [0 for _ in range(n+1)]

# d[i]= max(d[i-j]+cards[j])
for i in range(0, n+1):
    target = []
    for j in range(0, i+1):
        target.append(cards[j]+d[i-j])
    d[i] = max(target)

print(d[n])
