# 출처 : https://www.acmicpc.net/problem/11722
n = int(input())
numbers = list(map(int, input().split()))

# 뒤집으면 감소하는 방향
numbers.reverse()
# lis
d = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if(numbers[i] > numbers[j]):
            d[i] = max(d[i], d[j]+1)

print(max(d))
