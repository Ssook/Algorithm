# 출처 : https://www.acmicpc.net/problem/1939
from collections import deque

n, m = map(int, input().split())
graph = [{} for i in range(n)]
maxValue = 0
for i in range(m):
    a, b, w = map(int, input().split())
    maxValue = max(maxValue, w)
    key1 = str(b-1)
    key2 = str(a-1)
    if(key1 in graph[a-1]):
        graph[a-1][key1] = max(graph[a-1][key1], w)
        graph[b-1][key2] = max(graph[b-1][key2], w)
    else:
        graph[a-1][key1] = w
        graph[b-1][key2] = w


startNode, endNode = map(int, input().split())
startNode -= 1
endNode -= 1


def bfs(n, endNode, weight):
    queue = deque([n])
    visit[n] = True
    while(queue):
        cur = queue.popleft()
        if(cur == endNode):
            return True
        for key in graph[cur]:
            next = int(key)
            if(visit[next] == False and graph[cur][key] >= weight):
                queue.append(next)
                visit[next] = True
    return False


l = 1
r = maxValue
visit = [False for i in range(n)]
answer = 0
while(r >= l):
    mid = (r+l)//2
    visit = [False for i in range(n)]

    if(bfs(startNode, endNode, mid)):
        answer = max(answer, mid)
        l = mid+1
    else:
        r = mid-1
print(answer)
