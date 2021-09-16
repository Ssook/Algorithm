from collections import deque
n, m = map(int, input().split())
floor = []
for i in range(n):
    floor.append(list(input()))


answer = 0
for i in range(n):
    queue = deque()
    countWidth = 0
    for j in range(m):
        if(not queue and floor[i][j] == '-'):
            countWidth += 1
        if(queue):
            now = queue.popleft()
            if(floor[i][j] != now and floor[i][j] == '-'):
                countWidth += 1
        queue.append(floor[i][j])
    answer += countWidth


for j in range(m):
    queue = deque()
    countHeight = 0
    for i in range(n):
        if(not queue and floor[i][j] == '|'):
            countHeight += 1
        if(queue):
            now = queue.popleft()
            if(floor[i][j] != now and floor[i][j] == '|'):
                countHeight += 1
        queue.append(floor[i][j])
    answer += countHeight

print(answer)
