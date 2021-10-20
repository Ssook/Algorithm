# 출처 : https://www.acmicpc.net/problem/2670
n = int(input())
numbers = []
answer = 0
for i in range(n):
    numbers.append(float(input()))

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i]*numbers[i-1])
    if(numbers[i] > answer):
        answer = numbers[i]

print("{:.3f}".format(max(numbers)))
