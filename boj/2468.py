# 출처 : https://www.acmicpc.net/problem/2468
# 재귀호출 제한
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

n = int(input())
answer = []
graph = []
# 비오는 높이의 최대값 정하기 위해 사용
maxHeight = 0
for i in range(n):
    line = list(map(int, input().split(' ')))
    maxHeight = max(maxHeight, max(line))
    graph.append(line)

# 상하좌우
deltaList = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y, copyGraph):
    copyGraph[x][y] = 0
    for d in deltaList:
        if(x+d[0] >= 0 and x+d[0] < n and y+d[1] >= 0 and y+d[1] < n):
            if(copyGraph[x+d[0]][y+d[1]] > 0):
                dfs(x+d[0], y+d[1], copyGraph)


# 반복문을 돌면서 높이를 올리면서, 일정 높이 이하의 칸들은 다 0으로 바꾸고 dfs 진행,
for i in range(1, maxHeight):
    count = 0
    copyGraph = deepcopy(graph)

    for x in range(n):
        for y in range(n):
            if(copyGraph[x][y] <= i):
                copyGraph[x][y] = 0
    # print(copyGraph)

    for x in range(n):
        for y in range(n):
            if(copyGraph[x][y] > 0):
                count += 1
                dfs(x, y, copyGraph)
    answer.append(count)

if(len(answer) == 0):
    print(1)
else:
    print(max(answer))
