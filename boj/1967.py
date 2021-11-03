# 출처 : https://www.acmicpc.net/problem/1967
from collections import deque
global answer, longestNode
answer = 0
longestNode = 0

n = int(input())
# 노드가 하나일 경우 0
if(n == 1):
    print(0)
    exit()
graphDict = {}
parent = [0 for i in range(n+1)]
check = [0 for i in range(n+1)]


for i in range(n-1):
    a, b, cost = map(int, input().split())
    if(str(a) in graphDict):
        graphDict[str(a)].append((b, cost))
    else:
        graphDict[str(a)] = [(b, cost)]

    if(str(b) in graphDict):
        graphDict[str(b)].append((a, cost))
    else:
        graphDict[str(b)] = [(a, cost)]


def bfs(start):
    global answer, longestNode
    answer = 0
    longestNode = 0
    queue = deque([start])
    costs = deque([0])
    visit = [0 for i in range(n+1)]
    visit[start] = 1
    while(queue):
        cur = queue.popleft()
        cost = costs.popleft()
        if(answer <= cost):
            answer = cost
            longestNode = cur
        for path in graphDict[str(cur)]:
            node = path[0]
            weight = path[1]
            if(visit[node] == 0):
                queue.append(node)
                costs.append(cost+weight)
                visit[node] = 1


# 한 점에서 bfs를 통해 가장 멀리 있는 노드를 찾고, 해당 노드로부터 한번 더 bfs를 수행한다.
bfs(1)
bfs(longestNode)
print(answer)
