# 출처 : https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
parent = [i for i in range(0, n+1)]
answer = []

# 유니온 파인드


def find(x):
    if(x == parent[x]):
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y


for i in range(m):
    cmd, a, b = map(int, input().split())
    if(cmd == 0):
        union(a, b)
    if(cmd == 1):
        if(find(a) == find(b)):
            answer.append('YES')
        else:
            answer.append('NO')

for a in answer:
    print(a)
