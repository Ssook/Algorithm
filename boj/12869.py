# 출처 : https://www.acmicpc.net/problem/12869
from collections import deque
from itertools import permutations

n = int(input())
hp = list(map(int, input().split()))
for i in range(3-n):
    hp.append(0)
visit = [[[0 for i in range(61)] for j in range(61)] for k in range(61)]
hp.sort(reverse=True)

visit[hp[0]][hp[1]][hp[2]] = 1
counts = deque([0])
queue = deque([hp])

# bfs
while(queue):
    cur = queue.popleft()
    count = counts.popleft()
    flag = True

    # 모든 scv가 파괴되었는지 체크
    for i in range(3):
        if(cur[i] > 0):
            flag = False
    if(flag):
        print(count)
        break

    # 현재 체력 상태에서 갈 수 있는 상태들 방문 체크해서 큐에 넣어줌
    for c in permutations(cur, 3):
        newState = [0, 0, 0]
        if(c[0] > 0):
            newState[0] = c[0]-9
        if(c[1] > 0):
            newState[1] = c[1]-3
        if(c[2] > 0):
            newState[2] = c[2]-1
        newState.sort(reverse=True)

        if(visit[newState[0]][newState[1]][newState[2]] == 0):
            visit[newState[0]][newState[1]][newState[2]] = 1
            queue.append(newState)
            counts.append(count+1)
