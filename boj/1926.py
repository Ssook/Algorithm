# 출처 : https://www.acmicpc.net/problem/1926
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
drawCount = 0
answer = [0]

visit = [[0 for i in range(m)] for j in range(n)]


def bfs(x, y):
    count = 0
    queue = deque([(x, y)])
    visit[x][y] = 1
    while(queue):
        curX, curY = queue.popleft()
        graph[curX][curY] = 0
        count += 1
        for move in moves:
            nX, nY = curX+move[0], curY+move[1]
            if(0 <= nX < n and 0 <= nY < m and graph[nX][nY] == 1 and visit[nX][nY] == 0):
                queue.append((nX, nY))
                visit[nX][nY] = 1

    return count


for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            drawCount += 1
            c = bfs(i, j)

            answer.append(c)

print(drawCount)
print(max(answer))


# dfs 왜 메모리 초과 나는지 모르겠다.
# import sys
# sys.setrecursionlimit(82500)
# n, m = map(int, sys.stdin.readline().split())

# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# drawCount = 0
# answer = [0]


# def dfs(x, y):
#     count = 1
#     graph[x][y] = 0
#     for move in moves:
#         nX = x+move[0]
#         nY = y+move[1]
#         if (0 <= nX < n and 0 <= nY < m and graph[nX][nY] == 1):
#             count += dfs(nX, nY)

#     return count


# for i in range(n):
#     for j in range(m):
#         if(graph[i][j] == 1):
#             drawCount += 1
#             c = dfs(i, j)
#             answer.append(c)
#             # for g in graph:
#             #     print(g)
#             # print('----')
# print(drawCount)
# print(max(answer))
