# 출처 : https://www.acmicpc.net/problem/2294
n, k = map(int, input().split())
coins = list(set([int(input()) for _ in range(n)]))
INF = 987654321
d = [INF for i in range(k+1)]

for c in coins:
    if(k >= c):
        d[c] = 1

# 1,2,3,4...k원 반복
for i in range(k+1):
    # 사용할수 있는 동전들 보면서
    for coin in coins:
        count = 1
        # 해당 동전 여러개 쓰는 경우를 통해 dp
        while(i-count*coin > 0):
            # ex) 3,5,7원을 갖고 있을 때 12원을 만드는 방법은 min(d[12-3]+1,d[12-6]+2,d[12-5]+1,d[12-7]+1 ...)
            d[i] = min(d[i], d[i-coin*count]+count)
            count += 1


if(d[-1] == INF):
    print(-1)
else:
    print(d[-1])
