# 출처 : https://www.acmicpc.net/problem/7569
from collections import deque

# 모든 토마토가 익었는지 확인하는 함수


def check(h, x, y):
    for i in range(h):
        for j in range(x):
            for k in range(y):
                if(totalGraph[i][j][k] == 0):
                    return False
    return True


m, n, h = map(int, input().split())
totalGraph = []
# 3중 그래프 만들기
for _ in range(h):
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    totalGraph.append(graph)

visit = [[[0 for i in range(m)] for j in range(n)] for k in range(h)]
answer = 0

# 위아래 경로 추가
moves = [[0, 0, -1], [0, 0, 1], [1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0]]
queue = deque([])
costs = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(totalGraph[i][j][k] == 1):
                queue.append((i, j, k))
                costs.append(0)
                visit[i][j][k] = 1


# bfs수행
while(queue):
    height, x, y = queue.popleft()
    cost = costs.popleft()
    for move in moves:
        if(move[0]+height >= 0 and move[0]+height < h and move[1]+x >= 0 and move[1]+x < n and move[2]+y >= 0 and move[2]+y < m and totalGraph[move[0]+height][move[1]+x][move[2]+y] == 0):
            queue.append((move[0]+height, move[1]+x, move[2]+y))
            totalGraph[move[0]+height][move[1]+x][move[2]+y] = 1
            costs.append(cost+1)


if(check(h, n, m)):
    print(cost)
else:
    print(-1)
