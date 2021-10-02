# 출처 : https://www.acmicpc.net/problem/11399
n = int(input())
waitList = list(map(int, input().split()))

waitList.sort()
answer = 0
total = 0
for w in waitList:
    total += w
    answer += total

print(answer)
