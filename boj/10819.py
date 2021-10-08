# 출처 : https://www.acmicpc.net/problem/10819
from itertools import permutations
n = int(input())
numbers = list(map(int, input().split()))
# 순열 구해서 완전탐색
test = list(permutations(numbers, len(numbers)))

answer = 0
for t in test:
    count = 0
    for i in range(n-1):
        count += abs(t[i]-t[i+1])
    answer = max(answer, count)

print(answer)
