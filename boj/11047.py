# 출처 : https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())
money = []

for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)

answer = 0
for m in money:
    answer += k//m
    k -= m*(k//m)

print(answer)
