# 출처 : https://www.acmicpc.net/problem/11055
n = int(input())
numbers = list(map(int, input().split()))
d = [numbers[i] for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if(numbers[i] > numbers[j]):
            d[i] = max(d[i], d[j]+numbers[i])


print(max(d))
