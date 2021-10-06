# 출처 : https://www.acmicpc.net/problem/10026
import copy
import sys
sys.setrecursionlimit(10000)
# 그래프 그리기
n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))
originGraph = copy.deepcopy(graph)
normal = 0  # 일반인
color = 0  # 색맹
# 상하좌우
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 색마다 다른 색으로 준다.
rgb = {
    'R': '1',
    'G': '2',
    'B': '3'
}


def dfs(x, y, number):
    alphabet = graph[x][y]
    graph[x][y] = number
    for move in moves:
        if(x+move[0] >= 0 and x+move[0] < n and y+move[1] >= 0 and y+move[1] < n):
            if(graph[x+move[0]][y+move[1]] in rgb and rgb[graph[x+move[0]][y+move[1]]] == rgb[alphabet]):
                dfs(x+move[0], y+move[1], number)


# 일반인버전 dfs 수행
for i in range(n):
    for j in range(n):
        if(graph[i][j] in rgb):
            dfs(i, j, rgb[graph[i][j]])
            normal += 1

# 색맹은 R과 G가 붙어있으면 같은색으로 보이므로 value를 동일하게 해준다.
rgb = {
    'R': '1',
    'G': '1',
    'B': '3'
}
# 원래 그래프로 다시 복구
graph = copy.deepcopy(originGraph)

# 색맹버전으로 다시 dfs 수행
for i in range(n):
    for j in range(n):
        if(graph[i][j] in rgb):
            dfs(i, j, rgb[graph[i][j]])
            color += 1

print(normal, color)
