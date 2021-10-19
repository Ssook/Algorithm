# 출처 : https://www.acmicpc.net/problem/9935
from collections import deque
a = deque(list(input()))
b = list(input())
stack = []
while(a):
    stack.append(a.popleft())
    if(stack[-len(b):] == b):
        stack[-len(b):] = []

if(stack):
    print(''.join(stack))
else:
    print('FRULA')
