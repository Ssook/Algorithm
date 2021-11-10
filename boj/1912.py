# 출처 : https://www.acmicpc.net/problem/1912
n = int(input())
numbers = list(map(int, input().split()))
total = 0

for num in numbers:
    total += num

d = [0 for i in range(n)]
d[0] = numbers[0]

for i in range(1, n):
    d[i] = max(d[i-1]+numbers[i], numbers[i])

print(max(d))
