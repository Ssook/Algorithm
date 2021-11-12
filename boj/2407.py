# 출처 : https://www.acmicpc.net/problem/2407
import math
n, m = map(int, input().split())

def ncr(n, r):
    a = (math.factorial(n)//(math.factorial(n-r)*math.factorial(r)))
    return a


print(int(ncr(n, m)))
