# 출처 : https://www.acmicpc.net/problem/1005

from collections import deque
t = int(input())
answer = []
for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    times.insert(0, 0)
    indegrees = [0 for i in range(n+1)]
    indegrees[0] = 999
    graphDict = {}

    for i in range(k):
        x, y = map(int, input().split())
        if(str(x) in graphDict):
            graphDict[str(x)].append(y)
        else:
            graphDict[str(x)] = [y]
        indegrees[y] += 1

    target = int(input())

    queue = deque([])
    costs = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if(indegrees[i] == 0):
            queue.append(i)
            costs[i] = times[i]

    while(queue):
        cur = queue.popleft()

        if(cur == target):
            answer.append(costs[cur])
            break
        if(str(cur) in graphDict):
            for node in graphDict[str(cur)]:
                indegrees[node] -= 1
                if(indegrees[node] == 0):
                    queue.append(node)
                costs[node] = max(costs[node], costs[cur]+times[node])


for a in answer:
    print(a)
