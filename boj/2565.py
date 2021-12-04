# 출처 : https://www.acmicpc.net/problem/2565
line = [list(map(int, input().split())) for _ in range(int(input()))]
line.sort(key=lambda x: (x[0]))
numbers = [line[i][1] for i in range(len(line))]

d = [1 for _ in range(len(line))]
d2 = [1 for _ in range(len(line))]

# lis
for i in range(1, len(line)):
    for j in range(i):
        if(numbers[i] > numbers[j]):
            d[i] = max(d[i], d[j]+1)


print(len(line)-max(d))
