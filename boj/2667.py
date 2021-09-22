# 출처 : https://www.acmicpc.net/problem/2667
answer = 0
counts = []
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y, count):
    # 집 개수 세는 count
    if(x < 0 or y < 0 or x >= n or y >= n):
        return count
    if(graph[x][y] != 1):
        return count

    graph[x][y] = 0
    count += 1
    count = dfs(x, y+1, count)
    count = dfs(x+1, y, count)
    count = dfs(x-1, y, count)
    count = dfs(x, y-1, count)

    return count


for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            answer += 1
            counts.append(dfs(i, j, 0))
print(answer)
counts.sort()
for i in counts:
    print(i)
