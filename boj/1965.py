# 출처 : https://www.acmicpc.net/problem/1965
n = int(input())
numbers = list(map(int, input().split()))
d = [1 for _ in range(n+1)]

# lis
for i in range(1, n):
    for j in range(i):
        if(numbers[i] > numbers[j]):
            d[i] = max(d[i], d[j]+1)

print(max(d))
