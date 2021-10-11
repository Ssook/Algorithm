# 출처 : https://www.acmicpc.net/problem/9019
from collections import deque
t = int(input())
dict = {'0': 'D', '1': 'S', '2': 'L', '3': 'R'}
answer = []

# R연산


def right(n):
    n = str(n)
    n = n.zfill(4)
    return int(n[3]+n[0:3])

# L연산


def left(n):
    n = str(n)
    n = n.zfill(4)
    return int(n[1:4]+n[0])


for _ in range(t):
    start, target = map(int, input().split())
    visit = [0 for a in range(10000)]
    queue = deque([start])
    costs = deque([0])
    commands = deque([''])
    visit[start] = 1
    # bfs
    while(queue):
        cur = queue.popleft()
        cost = costs.popleft()
        command = commands.popleft()
        if(cur == target):
            # 값 찾으면 지금까지의 명령들을 딕셔너리를 이용해 변환해서 answer리스트에 추가
            st = ''
            for ll in list(str(command)):
                st += dict[ll]
            answer.append(st)
            break
        d = cur*2
        if(d >= 10000):
            d = d % 10000

        s = cur-1
        if(cur == 0):
            s = 9999
        l = left(cur)
        r = right(cur)
        moves = [d, s, l, r]
        for m in range(len(moves)):
            if(visit[moves[m]] == 0):
                costs.append(cost+1)
                queue.append(moves[m])
                commands.append(command+str(m))
                visit[moves[m]] = 1

for a in answer:
    print(a)
