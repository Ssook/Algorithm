# 출처 : https://www.acmicpc.net/problem/1976
n = int(input())
m = int(input())
parent = [i for i in range(n+1)]


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
    parent[pY] = pX


flag = True
graph = [list(map(int, input().split())) for i in range(n)]
path = list(map(int, input().split()))


for i in range(n):
    for j in range(n):
        if (graph[i][j] == 1):
            # 길이 이어져있으면 유니언
            union(i+1, j+1)


flag = True
# 시작점 노드의 부모
r = parent[path[0]]
# 경로의 모든 노드 부모가 시작점 노드의 부모랑 같으면 사이클
for p in path:
    if(parent[p] != r):
        flag = False

if(flag):
    print('YES')
else:
    print('NO')
