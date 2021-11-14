# 출처 : https://www.acmicpc.net/problem/12852
from collections import deque
n = int(input())

queue = deque([n])
visit = [0 for i in range(n+1)]
path = deque([str(n)])
counts = deque([0])
answer = ''
answerCount = 0
while(queue):
    cur = queue.popleft()
    p = path.popleft()
    c = counts.popleft()
    if(cur == 1):
        answerCount = c
        answer = p
        break
    if(cur % 3 == 0 and visit[cur//3] == 0):
        queue.append(cur//3)
        visit[cur//3]
        path.append(p+' '+str(cur//3))
        counts.append(c+1)
    if(cur % 2 == 0 and visit[cur//2] == 0):
        queue.append(cur//2)
        visit[cur//2]
        path.append(p+' '+str(cur//2))
        counts.append(c+1)
    if(visit[cur-1] == 0):
        queue.append(cur-1)
        visit[cur-1] = 0
        path.append(p+' '+str(cur-1))
        counts.append(c+1)
print(answerCount)
print(answer)
