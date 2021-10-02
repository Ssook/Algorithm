# 출처 : https://www.acmicpc.net/problem/5585
n = int(input())
n = 1000-n

change = [500, 100, 50, 10, 5, 1]
answer = 0
for c in change:
    answer += n//c
    n -= c * (n//c)

print(answer)
