# 출처 : https://www.acmicpc.net/problem/2251
from collections import deque
maxA, maxB, maxC = map(int, input().split())
answer = []

c = maxC
sum = c
visit = [[0 for i in range(maxC+1)]for j in range(maxC+1)]
queue = deque([(0, 0)])
# bfs
while(queue):
    curA, curB = queue.popleft()
    if(visit[curA][curB] == 1):
        continue

    visit[curA][curB] = 1
    curC = sum-curA-curB
    if(curA == 0 and (curC not in answer)):
        answer.append(curC)

    # a->b
    if(maxB >= curA+curB):
        queue.append((0, curA+curB))
    else:
        queue.append((curA-(maxB-curB), maxB))
    # a->c
    if(maxC >= curA+curC):
        queue.append((0, curB))
    else:
        queue.append((curA-(maxC-curC), curB))
    # b->a
    if(maxA >= curA+curB):
        queue.append((curA+curB, 0))
    else:
        queue.append((maxA, curB-(maxA-curA)))
    # b->c
    if(maxC >= curB+curC):
        queue.append((curA, 0))
    else:
        queue.append((curA, curB-(maxC-curC)))
    # c->b
    if(maxB >= curB+curC):
        queue.append((curA, curB+curC))
    else:
        queue.append((curA, maxB))
    # c->a
    if(maxA >= curC+curA):
        queue.append((curC+curA, curB))
    else:
        queue.append((maxA, curB))

answer.sort()
for a in answer:
    if(a != answer[-1]):
        print(a, end=' ')
    else:
        print(a)
