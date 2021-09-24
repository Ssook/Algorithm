# 출처 : https://www.acmicpc.net/problem/14502

from copy import deepcopy
from itertools import combinations
from collections import deque

# 전염이 완료된 후, 0의 갯수를 구하는 함수


def countZero(copyGraph):
    count = 0
    for i in range(n):
        for j in range(m):
            if(copyGraph[i][j] == 0):
                count += 1
    return count


n, m = map(int, input().split(' '))
answer = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split(' '))))

# 0이 위치한 좌표를 구해서 벽을 세울 수 있는 모든 조합을 만든다.
zeroList = []
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            zeroList.append([i, j])
# print(zeroList)
combinations = (list(combinations(zeroList, 3)))

# 상하좌우를 위한
deltaList = [[-1, 0], [1, 0], [0, 1], [0, -1]]

# 1. 조합중에 하나 선택해서 벽을 세우고, 2. 전염병 돌리고, 3. 0의 갯수 체크
for combi in combinations:
    visit = [[0 for i in range(m)] for j in range(n)]
    copyGraph = deepcopy(graph)

    # 조합에서 하나 골라서 벽세우는 과정
    for point in combi:
        copyGraph[point[0]][point[1]] = 1

    # bfs로 전염병 돌리기
    queue = deque()
    for x in range(n):
        for y in range(m):
            if(copyGraph[x][y] == 2):
                visit[x][y] = 1
                queue.append([x, y])
    while(queue):
        curPoint = queue.popleft()
        copyGraph[curPoint[0]][curPoint[1]] = 2
        visit[curPoint[0]][curPoint[1]] = 1
        x = curPoint[0]
        y = curPoint[1]
        for d in deltaList:
            if(x+d[0] >= 0 and x+d[0] < n and y+d[1] >= 0 and y+d[1] < m):
                if(copyGraph[x+d[0]][y+d[1]] == 0):
                    queue.append([x+d[0], y+d[1]])

    # 전염병이 돌고나서 0의 갯수 체크
    answer.append(countZero(copyGraph))
print(max(answer))
