# 출처 : https://www.acmicpc.net/submit/1916
n = int(input())
m = int(input())
INF = 987654321
roadDict = {}
graph = [[INF for i in range(n)] for j in range(n)]
check = [0 for i in range(n)]
distance = [INF for i in range(n)]

for i in range(m):
    a, b, d = map(int, input().split())
    if(graph[a-1][b-1] == INF):
        graph[a-1][b-1] = d
    else:
        graph[a-1][b-1] = min(graph[a-1][b-1], d)


start, end = map(int, input().split())
start -= 1
end -= 1
distance[start] = 0

# 다익스트라 수행
for i in range(n-1):
    minDistance = INF+1
    nowIndex = -1
    for j in range(len(distance)):
        if(check[j] == 0 and distance[j] < minDistance):
            minDistance = distance[j]
            nowIndex = j

    check[nowIndex] = 1
    for k in range(len(graph[nowIndex])):
        if(distance[nowIndex]+graph[nowIndex][k] < distance[k]):
            distance[k] = distance[nowIndex]+graph[nowIndex][k]

print(distance[end])
