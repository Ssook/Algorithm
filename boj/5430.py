# 출처 : https://www.acmicpc.net/problem/5430
from collections import deque
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    command = list(sys.stdin.readline())
    numberLength = int(sys.stdin.readline())
    numbers = sys.stdin.readline()
    numbers = numbers[1:-2]
    if(numberLength == 0):
        numbers = []
    else:
        numbers = list(map(int, numbers.split(',')))
    queue = deque(numbers)
    command = deque(command)
    isR = command.count('R') % 2
    # flag값을 바꾸면서 popleft를 할지 pop을 할지 정함
    flag = True
    isE = False
    while(command):
        cur = command.popleft()
        if(cur == 'D'):
            if(queue):
                if(flag):
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                isE = True
                break
        if(cur == 'R'):
            flag = not flag
    if not isE:
        if isR:
            queue.reverse()
        print('[', end='')
        for i in range(len(queue)):
            if(i == len(queue)-1):
                print(queue[i], end='')
            else:
                print(queue[i], end=',')
        print(']')
