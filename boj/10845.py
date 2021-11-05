# 출처 : https://www.acmicpc.net/problem/10845
from collections import deque

n = int(input())
answer = []
queue = deque([])
for i in range(n):
    cmd = input()
    if('push' in cmd):
        no = int(cmd.split()[1])
        queue.append(no)
    elif(cmd == 'front'):
        if(queue):
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif(cmd == 'back'):
        if(queue):
            answer.append(queue[-1])
        else:
            answer.append(-1)

    elif(cmd == 'pop'):
        if(queue):
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif(cmd == 'empty'):
        if(queue):
            answer.append(0)
        else:
            answer.append(1)
    elif(cmd == 'size'):
        answer.append(len(queue))


for a in answer:
    print(a)
