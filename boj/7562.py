# 출처 : https://www.acmicpc.net/problem/7562
from collections import deque
t = int(input())
answer = []
moves = [[1, 2], [2, 1], [2, -1], [1, -2],
         [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
for _ in range(t):
    n = int(input())
    curX, curY = map(int, input().split())
    targetX, targetY = map(int, input().split())

    visit = [[0 for i in range(n)] for j in range(n)]
    visit[curX][curY] = 1
    costs = deque([0])

    queue = deque([(curX, curY)])
    while(queue):
        curX, curY = queue.popleft()
        cost = costs.popleft()
        if(curX == targetX and curY == targetY):
            answer.append(cost)
            break
        for move in moves:
            if(curX+move[0] >= 0 and curX+move[0] < n and curY+move[1] >= 0 and curY+move[1] < n and visit[curX+move[0]][curY+move[1]] == 0):
                queue.append((curX+move[0], curY+move[1]))
                visit[curX+move[0]][curY+move[1]] = 1
                costs.append(cost+1)

for a in answer:
    print(a)
