# 출처 : https://www.acmicpc.net/problem/1507
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

usePath = [[1 for i in range(n)] for j in range(n)]
# 플로이드 역으로 사용
for k in range(n):
    for i in range(n):
        if(i == k):
            continue
        for j in range(n):
            if(i == j or j == k):
                continue
            if(graph[i][j] > graph[i][k]+graph[k][j]):
                print(-1)
                exit(0)
            if(graph[i][j] == graph[i][k]+graph[k][j]):
                usePath[i][j] = 0


answer = 0
for i in range(n):
    for j in range(n):
        if(usePath[i][j] == 1):
            answer += graph[i][j]

print(answer//2)
