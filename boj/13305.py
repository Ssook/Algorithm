# 출처 : https://www.acmicpc.net/problem/13305
answer = 0
n = int(input())
road = list(map(int, input().split()))
costs = list(map(int, input().split()))
# 현재 주유 가능한 값들
possibleCosts = []

# 각 칸에 갈때마다 주유 가능한 값들 중 최소의 값을 더함
for r in road:
    possibleCosts.append(costs.pop(0))
    answer += r*min(possibleCosts)

print(answer)
