# 출처 : https://www.acmicpc.net/problem/1059
l = int(input())
s = list(map(int, input().split()))
n = int(input())
s.sort()
if(n in s):
    print(0)
else:
    maxV = 0
    minV = 9999
    for i in range(l):
        if (s[i] > n):
            minV = min(minV, s[i])
        if(s[i] < n):
            maxV = max(maxV, s[i])

    minV -= 1
    maxV += 1
    answer = 0
    for i in range(maxV, minV+1):
        for j in range(minV, i, -1):
            start = i
            end = j
            if(start <= n and n <= end):
                answer += 1

    print(answer)
