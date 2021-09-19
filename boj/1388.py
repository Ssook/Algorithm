# 출처 : https://www.acmicpc.net/problem/1388

from collections import deque
n, m = map(int, input().split())
floor = []
# 맵 만들기
for i in range(n):
    floor.append(list(input()))


answer = 0

# 가로 구하는 과정(한 행씩 보면서)
for i in range(n):
    queue = deque()
    countWidth = 0
    for j in range(m):
        # 큐에 아무 것도 없고 -이면 카운트 증가
        if(not queue and floor[i][j] == '-'):
            countWidth += 1
        #
        if(queue):
            now = queue.popleft()

            # 이어지지 않는 경우 카운트 증가
            if(floor[i][j] != now and floor[i][j] == '-'):
                countWidth += 1
        queue.append(floor[i][j])
    answer += countWidth

# 세로 구하는 과정(위와 동일)
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
