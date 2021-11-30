# 출처 : https://www.acmicpc.net/problem/1158
from collections import deque
n, k = map(int, input().split())
numbers = deque(list(range(1, n+1)))

idx = k-1
answer = []
while(numbers):
    for i in range(idx):
        numbers.append(numbers.popleft())
    answer.append(numbers.popleft())


print('<', end='')
for i in range(n-1):
    print(answer[i], end=', ')
print(answer[-1], end='>')
