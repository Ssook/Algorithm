# 출처 : https://www.acmicpc.net/problem/13398
n = int(input())
numbers = list(map(int, input().split()))
d = [[0 for i in range(n)] for j in range(2)]
d[0][0] = numbers[0]
# d[0]은 숫자를 제거하지 않는 dp, d[1]은 숫자를 하나 제거한 dp
answer = numbers[0]

for i in range(1, n):
    d[0][i] = max(d[0][i-1]+numbers[i], numbers[i])  # 이전 dp값에 현재 숫자를 더한 결과와 새로 시작하는 경우 비교
    d[1][i] = max(d[0][i-1], d[1][i-1]+numbers[i]) # 현재숫자를 제거한 경우와 제거하지 않은 경우 비교
    answer = max(d[0][i], d[1][i], answer)


print(answer)
