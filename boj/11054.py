# 출처 : https://www.acmicpc.net/problem/11054
n = int(input())
numbers = list(map(int, input().split()))

# lis
d = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if(numbers[i] > numbers[j]):
            d[i] = max(d[i], d[j]+1)


# lis 거꾸로
d2 = [1 for i in range(n)]
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if(numbers[i] > numbers[j]):
            d2[i] = max(d2[i], d2[j]+1)


answer = [0 for i in range(n)]

for i in range(n):
    answer[i] = d[i]+d2[i]

print(max(answer)-1)
