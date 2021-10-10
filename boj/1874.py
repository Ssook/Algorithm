# 출처 : https://www.acmicpc.net/problem/1874
n = int(input())
stack = []
target = []
answer = []
for i in range(n):
    target.append(int(input()))

index = 0
maximum = 0
for i in range(1, len(target)+1):
    stack.append(i)
    answer.append('+')
    while(target[index] == stack[-1]):
        answer.append('-')

        stack.pop()
        index += 1
        if(not stack):
            break

if(stack):
    print('NO')
else:
    for p in answer:
        print(p)
