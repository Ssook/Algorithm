# 출처 : https://www.acmicpc.net/problem/1509

import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
d = [[0 for i in range(n)] for j in range(n)]
# 하나인 경우
for i in range(n):
    d[i][i] = 1
# 두개인 경우
for i in range(n-1):
    if(numbers[i] == numbers[i+1]):
        d[i][i+1] = 1
# 세개이상인 경우
for k in range(3, n+1):
    for i in range(n-k+1):
        if(numbers[i] == numbers[i+k-1] and d[i+1][i+k-2] == 1):
            d[i][i+k-1] = 1
m = int(sys.stdin.readline())
answer = []
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    answer.append(d[s-1][e-1])

for a in answer:
    print(a)
