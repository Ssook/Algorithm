# 출처 : https://www.acmicpc.net/problem/9205
from collections import deque
t = int(input())
answerArr = []

for _ in range(t):
    answer = False
    n = int(input())
    homeX, homeY = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    rockX, rockY = map(int, input().split())

    # 집이랑 도착점 리스트에 붙여줌
    stores.insert(0, [homeX, homeY])
    stores.append([rockX, rockY])
    visit = [0 for j in range(n+2)]
    graph = [[0 for i in range(n+2)] for j in range(n+2)]

    # 각 지점마다 거리계산
    for i in range(n+2):
        for j in range(n+2):
            if(i != j):
                graph[i][j] = abs(stores[j][0]-stores[i][0]) + \
                    abs(stores[j][1]-stores[i][1])

    visit[0] = 1
    queue = deque([0])
    while(queue):
        cur = queue.popleft()
        if(cur == n+1):
            answer = True
            break

        # 현재점에서 1000m안에 갈 수 있는 장소를 큐에 넣어준다.
        for i in range(len(graph[cur])):
            if(graph[cur][i] <= 1000 and visit[i] == 0):
                queue.append(i)
                visit[i] = 1

    if(answer):
        answerArr.append('happy')
    else:
        answerArr.append('sad')

for a in answerArr:
    print(a)
