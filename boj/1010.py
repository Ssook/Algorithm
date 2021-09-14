from itertools import combinations


def comb(n, m):
    sum = 1
    divider = 1
    while n > 0:
        sum *= m
        divider *= n
        m -= 1
        n -= 1
    return int(sum/divider)
# 3, 4
# 2, 3
# 1, 2


T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    print(comb(N, M))
