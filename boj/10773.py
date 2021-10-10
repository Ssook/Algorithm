# 출처 : https://www.acmicpc.net/problem/10773
k = int(input())
stack = []
for i in range(k):
    n = int(input())
    if(n != 0):
        stack.append(n)
    else:
        stack.pop()
answer = 0
for s in stack:
    answer += s

print(answer)
