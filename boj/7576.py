from collections import deque

# 그래프 그리는 과정
m, n = map(int, input().split())

graph = []
for i in range(n):
    line = list(map(int, input().split(' ')))
    graph.append(line)

# 이미 모든 토마토가 익은 경우 처리
allTomato = True
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if(graph[i][j] == 0):
            allTomato = False

if(allTomato):
    print('0')

# 모든 토마토가 안 익은 경우
else:
    # x,y 큐를 따로 두고 bfs 진행
    xQueue = deque()
    yQueue = deque()
    count = 0
    counts = deque()

    # 모든 익은 토마토의 좌표와 개수만큼의 카운트를 큐에 넣음
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if(graph[i][j] == 1):
                xQueue.append(i)
                yQueue.append(j)
                counts.append(count)
    answer = 0

    # bfs 진행
    while(xQueue and yQueue):
        curX = xQueue.popleft()
        curY = yQueue.popleft()
        curCount = counts.popleft()
        answer = curCount

        # 상하좌우 확인하고 bfs큐에 넣음
        if(curX-1 >= 0 and graph[curX-1][curY] == 0):
            graph[curX-1][curY] = 1
            xQueue.append(curX-1)
            yQueue.append(curY)
            counts.append(curCount+1)

        if(curX+1 < n and graph[curX+1][curY] == 0):
            graph[curX+1][curY] = 1
            xQueue.append(curX+1)
            yQueue.append(curY)
            counts.append(curCount+1)

        if(curY-1 >= 0 and graph[curX][curY-1] == 0):
            graph[curX][curY-1] = 1
            xQueue.append(curX)
            yQueue.append(curY-1)
            counts.append(curCount+1)

        if(curY+1 < m and graph[curX][curY+1] == 0):
            graph[curX][curY+1] = 1
            xQueue.append(curX)
            yQueue.append(curY+1)
            counts.append(curCount+1)

    # bfs를 다 진행하고나서, 한개라도 0 이 있으면 다 익을 수 없는 경우이므로 -1
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if(graph[i][j] == 0):
                answer = -1

    print(answer)
