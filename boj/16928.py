# 출처 : https://www.acmicpc.net/problem/16928
from collections import deque

n,m = map(int,input().split())

stairs = {}
snakes = {}
for i in range(n):
    x,y = map(int,input().split())
    stairs[str(x)]=y

for i in range(m):
    x,y = map(int,input().split())
    snakes[str(x)]=y
answer = 0
queue = deque([1])
counts = deque([0])
visit = [0 for i in range(101)]
while(queue):
    count = counts.popleft()
    cur = queue.popleft()
    if(cur == 100):
        answer = count
        break
    for i in range(1,7):
        key = str(cur+i)
        if cur+i>100:
            break

        if(visit[cur+i]==0):
            if(key in stairs):
                queue.append(stairs[key])
            elif(key in snakes):
                queue.append(snakes[key])
            else :
                queue.append(cur+i)
            counts.append(count+1)
            visit[cur+i]=1

print(answer)