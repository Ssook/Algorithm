# 출처 : https://www.acmicpc.net/problem/15656
from itertools import product
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for p in product(numbers, repeat=m):
    print(*p)
