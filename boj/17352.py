# 출처 : https://www.acmicpc.net/problem/17352
n = int(input())
parent = [i for i in range(n+1)]


def find(x):
    if(x == parent[x]):
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    pX = find(x)
    pY = find(y)
    if(pX != pY):
        if(pX > pY):
            pX, pY = pY, pX
        parent[pY] = pX


for i in range(n-2):
    a, b = map(int, input().split())
    if(a > b):
        a, b = b, a
    union(a, b)


for i in range(n+1):
    parent[i] = find(parent[i])


for i in range(2, n+1):
    if(parent[i-1] != parent[i]):
        print(str(i-1)+' '+str(i))
        break
