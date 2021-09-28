from collections import deque

# 그래프 그리기
answer = 0
n, m = map(int, input().split())

graph = []
visit = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    graph.append(list(map(int, input())))

# x,y,distance
queue = deque([(0, 0, 1)])
# 상하좌우
move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
while(queue):
    curX, curY, distance = queue.popleft()
    graph[curX][curY] = distance
    # visit이 없으면 메모리 초과
    visit[curX][curY] = 1
    if(curX == n-1 and curY == m-1):
        answer = distance
    # 상하좌우에 길이 있으면 좌표와 거리를 큐에넣어줌
    for mov in move:
        if(curX+mov[0] >= 0 and curX+mov[0] < n and curY+mov[1] >= 0 and curY+mov[1] < m and graph[curX+mov[0]][curY+mov[1]] == 1 and visit[curX+mov[0]][curY+mov[1]] == 0):
            queue.append((curX+mov[0], curY+mov[1], distance+1))
            visit[curX+mov[0]][curY+mov[1]] = 1
print(answer)
