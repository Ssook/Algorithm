# 출처 : https://www.acmicpc.net/problem/14226
from collections import deque
s = int(input())

clipboards = deque([0])  # 클립보드 관리
queue = deque([1])  # 화면에 있는 이모티콘 수 관리
time = deque([0])  # 시간 관리
answer = 0
visit = [[0 for i in range(10001)] for j in range(10001)]  # visit 배열 크기 유의
visit[1][0] = 1  # 시작할때 1개가 화면에 있고 클립보드에 0개가 있음
while(queue):
    t = time.popleft()
    v = queue.popleft()
    c = clipboards.popleft()

    # 찾던 개수인 경우
    if(v == s):
        answer = t
        break

    # 3. 삭제하는 경우
    if(v > 0 and visit[v-1][c] == 0):
        time.append(t+1)
        queue.append(v-1)
        clipboards.append(c)
        visit[v-1][c] = 1
    # 2. 클립보드에 있는거 사용
    if(c > 0 and visit[v+c][c] == 0):
        queue.append(v+c)
        time.append(t+1)
        clipboards.append(c)
        visit[v+c][0] = 1

    # 1. 클립보드에 복사하는 경우
    if(visit[v][v] == 0):
        clipboards.append(v)
        queue.append(v)
        time.append(t+1)
        visit[v][v] = 1

print(answer)
