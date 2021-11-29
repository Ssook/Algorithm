# 출처 : https://www.acmicpc.net/problem/15988
# dp배열을 미리 구해놓고 각 t마다 answer에 넣어주기만 한다.
# t마다 dp 배열을 다시 만들면 시간 초과
d = [0 for _ in range(1000001)]
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 1000001):
    d[i] = ((d[i-1] % 1000000009+d[i-2] % 1000000009+d[i-3] % 1000000009))

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    answer.append(d[n] % 1000000009)

for a in answer:
    print(a)
