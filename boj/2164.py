# 출처 : https://www.acmicpc.net/problem/2164
from collections import deque
n = int(input())

numbers = deque([])
for i in range(1, n+1):
    numbers.append(str(i))

while(len(numbers) > 1):
    numbers.popleft()
    numbers.append(numbers.popleft())


print(numbers[0])
