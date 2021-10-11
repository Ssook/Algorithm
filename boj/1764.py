# 출처 : https://www.acmicpc.net/problem/1764
from collections import deque
n, m = map(int, input().split())
ear = []
see = []
answer = []
for i in range(n):
    ear.append(input())
for i in range(m):
    see.append(input())

ear.sort()
see.sort()

q1 = deque(ear)
q2 = deque(see)
while(q1 and q2):
    if(q1[0] > q2[0]):
        q2.popleft()
    elif(q1[0] < q2[0]):
        q1.popleft()
    elif(q1[0] == q2[0]):
        q1.popleft()
        answer.append(q2.popleft())

print(len(answer))
for a in answer:
    print(a)
