# 출처 : https://www.acmicpc.net/problem/2210
from collections import deque
graph = [list(input().split()) for _ in range(5)]
answer = []


def bfs(x, y):
    queue = deque([(x, y)])
    paths = deque([''])
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while(queue):
        path = paths.popleft()
        curX, curY = queue.popleft()
        if(len(path) == 6):
            if(path not in answer):
                answer.append(path)
        else:
            for move in moves:
                nX, nY = curX+move[0], curY+move[1]
                if(nX >= 0 and nX < 5 and nY >= 0 and nY < 5):
                    paths.append(path+graph[nX][nY])
                    queue.append((nX, nY))


for i in range(5):
    for j in range(5):
        bfs(i, j)

print(len(answer))
