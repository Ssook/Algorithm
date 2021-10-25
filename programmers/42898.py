# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    graph = []
    for i in range(n+1):
        graph.append([0 for j in range(m+1)])

    graph[1][1] = 1
    for p in puddles:
        graph[p[1]][p[0]] = -1

    # d[i][j]는 그 위에서 온 경우의 수와 왼쪽에서 온 경우의 수를 더함
    for i in range(1, n+1):
        for j in range(1, m+1):
            if((i != 1 or j != 1) and graph[i][j] != -1):
                if(graph[i-1][j] != -1):
                    graph[i][j] += graph[i-1][j]
                    graph[i][j] = graph[i][j] % 1000000007
                if(graph[i][j-1] != -1):
                    graph[i][j] += graph[i][j-1]
                    graph[i][j] = graph[i][j] % 1000000007

    return graph[n][m]
