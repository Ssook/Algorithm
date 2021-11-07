# 출처 : https://www.acmicpc.net/problem/1743
import sys
sys.setrecursionlimit(10000)
n, m, k = map(int, input().split())
graph = [[0 for i in range(m)]for j in range(n)]
answer = []
for i in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1


def dfs(x, y, index):
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    graph[x][y] = index

    for move in moves:
        if(x+move[0] >= 0 and x+move[0] < n and y+move[1] >= 0 and y+move[1] < m and graph[x+move[0]][y+move[1]] == 1):
            dfs(x+move[0], y+move[1], index)


idx = 2

# 연결된 칸들마다 다른 색으로 색칠해놓기
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            dfs(i, j, idx)
            idx += 1

# 가장 많은 거 찾기
for c in range(2, idx+1):
    count = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == c):
                count += 1
    answer.append(count)
print(max(answer))
