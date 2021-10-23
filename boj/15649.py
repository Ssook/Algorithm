# 출처 : https://www.acmicpc.net/problem/15649
from itertools import permutations

n,m = map(int,input().split())

for p in permutations((range(1,n+1)),m):
    a = str(p)
    a = a.replace("(","")
    a = a.replace(")","")
    a = a.replace(",","")
    print(a)

    