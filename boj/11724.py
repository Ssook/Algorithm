# 출처 : https://www.acmicpc.net/problem/11724
# 그래프 그리는 과정
n, m = map(int, input().split())
graph = [[0 for i in range(n)] for j in range(n)]
visit = [0 for i in range(n)]
for i in range(m):
    x, y = map(int, input().split(' '))
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1


def dfs(n):
    visit[n] = 1
    for i in range(len(graph[n])):
        if(graph[n][i] == 1 and visit[i] == 0):
            dfs(i)


answer = 0
# 사이클 돌면 카운트+
for i in range(n):
    if(visit[i] == 0):
        answer += 1
        dfs(i)

print(answer)
