# 출처 : https://www.acmicpc.net/problem/5052
answer = []
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input() for i in range(n)]
    numbers.sort()
    flag = True
    for i in range(n-1):
        if(numbers[i] in numbers[i+1] and numbers[i+1].index(numbers[i]) == 0):
            flag = False
            break

    if(flag):
        answer.append('YES')
    else:
        answer.append('NO')

for a in answer:
    print(a)
