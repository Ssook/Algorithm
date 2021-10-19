# # 방법 1
# # d[i][j] = d[i][k]+d[k][j]   #k+a[i][k]==j
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# d = [[0 for i in range(n)] for j in range(n)]
# d[0][0] = 1
# for i in range(n):
#     for j in range(n):
#         if(i == 0 and j == 0):
#             continue
#         for k in range(j):
#             if(graph[i][k]+k == j):

#                 d[i][j] += d[i][k]
#         for k in range(i):
#             if(graph[k][j]+k == i):
#                 d[i][j] += +d[k][j]
# print(d[n-1][n-1])

# 방법 2
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

d = [[0 for i in range(n)] for j in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        if(i+graph[i][j] < n):
            d[i+graph[i][j]][j] += d[i][j]
        if(j+graph[i][j] < n):
            d[i][j+graph[i][j]] += d[i][j]

print(d[n-1][n-1])
