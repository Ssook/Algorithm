# 출처 : https://www.acmicpc.net/problem/17413
from collections import deque
inputString = deque(list(input()))
stack = []
answer = ''
# 스택과 큐 이용해서 문제 조건대로 구현
while(inputString):
    cur = inputString.popleft()
    if(cur == '<'):
        while(stack):
            answer += stack.pop()

        answer += cur
        while(inputString[0] != '>'):
            answer += inputString.popleft()
        answer += inputString.popleft()
    elif(cur == ' '):
        while(stack):
            answer += stack.pop()
        answer += cur
    else:
        stack.append(cur)

while(stack):
    answer += stack.pop()
print(answer)
