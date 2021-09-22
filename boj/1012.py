# 출처 : https://www.acmicpc.net/problem/1012

# 재귀호출 제한
import sys
sys.setrecursionlimit(10000)

t = int(input())
answer = [0 for b in range(t)]


def dfs(x, y):
    if(x < 0 or y < 0 or x >= n or y >= m):
        return
    if(graph[x][y] == 0):
        return
    graph[x][y] = 0

    # print(x, y,  '!', graph[x][y])
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y-1)


for a in range(t):
    # 맵 그리는 과정
    m, n, k = map(int, input().split())
    if(k == 0):
        answer[a] = 0
        break
    graph = [[0 for i in range(m)] for j in range(n)]

    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    # 맵 전체 탐색하면서 1인거 발견하면 dfs, dfs하면 그 땅과 연결된 모든것이 다 0으로 바뀌므로 독립된 영역이다.
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 1):
                answer[a] += 1
                dfs(i, j)


for ans in answer:
    print(ans)
