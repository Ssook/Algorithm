# 출처 : https://www.acmicpc.net/problem/18116

import sys
n = int(sys.stdin.readline())
parent = [i for i in range(1000001)]
count = [1 for i in range(1000001)]


def find(x):
    if(parent[x] == x):
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    pX = find(x)
    pY = find(y)
    if(pX > pY):
        pX, pY = pY, pX
    if(pX != pY):
        parent[pY] = pX
        # 노드의 개수도 같이 옮겨주어야 한다.
        count[pX] += count[pY]
        count[pY] = 0


for i in range(n):
    command = sys.stdin.readline().split()
    if(command[0] == 'I'):
        a, b = int(command[1]), int(command[2])
        if(a > b):
            a, b = b, a
        union(a, b)

    if(command[0] == 'Q'):
        c = int(command[1])
        print(count[find(c)])
