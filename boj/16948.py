# 출처 : https://www.acmicpc.net/problem/16948
from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

visit = [[0 for i in range(n)] for j in range(n)]
answer = -1
queue = deque([(r1, c1)])
counts = deque([0])
moves = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
while(queue):
    curR, curC = queue.popleft()
    count = counts.popleft()
    if(curR == r2 and curC == c2):
        answer = count
        break

    for move in moves:
        nX = curR+move[0]
        nY = curC+move[1]
        if(nX >= 0 and nX < n and nY >= 0 and nY < n and visit[nX][nY] == 0):
            queue.append((nX, nY))
            counts.append(count+1)
            visit[nX][nY] = 1

print(answer)
