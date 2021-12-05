# 출처 : https://www.acmicpc.net/problem/2003
n, m = map(int, input().split())
answer = 0
numbers = list(map(int, input().split()))

l = 0
r = 0
total = numbers[0]

while(l < n):
    if(total == m):
        answer += 1
        total -= numbers[l]
        l += 1

    elif(total < m):
        r += 1
        if(r == n):
            break
        total += numbers[r]

    elif(total > m):
        total -= numbers[l]
        l += 1

print(answer)
