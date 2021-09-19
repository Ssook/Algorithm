# 출처 : https://www.acmicpc.net/problem/2606
from collections import deque
n = int(input())
m = int(input())
visit = [0 for i in range(n)]
network = [[0 for i in range(n)] for j in range(n)]

# 네트워크 2차원 배열로 표현
for i in range(m):
    x, y = map(int, input().split())
    network[x-1][y-1] = 1
    network[y-1][x-1] = 1

# 큐 생성해서 bfs로 처리
queue = deque([0])
while(queue):
    curComputer = queue.popleft()
    visit[curComputer] = 1
    for i in range(n):
        if(network[curComputer][i] == 1 and visit[i] == 0):
            queue.append(i)

print(visit.count(1)-1)
