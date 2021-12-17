# 출처 : https://www.acmicpc.net/problem/1009
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    value = 1
    for i in range(b):
        value = (value*a) % 10

    if(value == 0):
        print(10)
    else:
        print(value)
