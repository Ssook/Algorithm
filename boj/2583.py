# 출처 : https://www.acmicpc.net/problem/2583
from collections import deque
m, n, k = map(int, input().split())
graph = [[0 for i in range(n)] for j in range(m)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1


moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def bfs(x, y):
    queue = deque([(x, y)])
    count = 0
    graph[x][y] = 1
    while(queue):
        curX, curY = queue.popleft()
        count += 1
        for move in moves:
            if(curX+move[0] >= 0 and curX+move[0] < m and curY+move[1] >= 0 and curY+move[1] < n and graph[curX+move[0]][curY+move[1]] == 0):
                queue.append((curX+move[0], curY+move[1]))
                graph[curX+move[0]][curY+move[1]] = 1

    return count


answer = []
for i in range(m):
    for j in range(n):
        if(graph[i][j] == 0):
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for a in answer:
    print(a, end=' ')
