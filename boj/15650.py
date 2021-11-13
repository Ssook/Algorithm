# 출처 : https://www.acmicpc.net/problem/15650
from itertools import combinations
n, m = map(int, input().split())
for combi in combinations(range(1, n+1), m):
    for c in combi:
        print(c, end=' ')
    print('')
