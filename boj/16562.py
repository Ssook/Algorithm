# 출처 : https://www.acmicpc.net/problem/16562
n, m, k = map(int, input().split())
parent = [i for i in range(n+1)]


def find(x):
    if parent[x] == x:
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


costs = list(map(int, input().split()))
graph = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    if(a > b):
        a, b = b, a
    union(a, b)


# 유니언 과정이 다 끝나고 한번 더 해주어야함
for i in range(len(parent)):
    parent[i] = parent[parent[i]]


pair = []
for i in range(n):
    pair.append([parent[i+1], costs[i]])

# 같은 집합, 코스트 순으로 정렬
pair.sort(key=lambda x: (x[0], x[1]))

start = 0
answer = 0
for i in range(n):
    # 각 분리 집합을 취할 수 있는 최소 비용 더하기
    if(pair[i][0] != start):
        start = pair[i][0]
        answer += pair[i][1]


if(answer > k):
    print('Oh no')

else:
    print(answer)
