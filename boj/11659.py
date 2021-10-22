# 출처 : https://www.acmicpc.net/problem/11659

import sys
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.insert(0, 0)
sum = 0
# 누적합 기록
for i in range(len(numbers)):
    sum += numbers[i]
    numbers[i] = sum

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(numbers[e]-numbers[s-1])
