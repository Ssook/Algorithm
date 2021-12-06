# 출처 : https://www.acmicpc.net/problem/1520
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# dp배열을 -1로 초기화
d = [[-1 for i in range(m)] for j in range(n)]

def dfs(x, y):
    # 도착점에 도달한 경우
    if(x == n-1 and y == m-1):
        return 1
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 아직 방문하지 않은 점인 경우 상하좌우에서 이 점에 올 수 있는 경우의 수를 누적한다.
    if(d[x][y] == -1):
        d[x][y] = 0
        for move in moves:
            nX = x+move[0]
            nY = y+move[1]
            if(nX >= 0 and nX < n and nY >= 0 and nY < m and graph[nX][nY] < graph[x][y]):
                d[x][y] += dfs(nX, nY)

    return d[x][y]


print(dfs(0, 0))
