# 출처 : https://www.acmicpc.net/problem/10974
from itertools import permutations
n = int(input())
numbers = range(1, n+1)
for p in permutations(numbers):
    print(*p)
