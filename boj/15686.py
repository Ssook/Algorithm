# 출처 : https://www.acmicpc.net/problem/15686
from itertools import combinations
n, m = map(int, input().split())

chickens = []
houses = []
global answer
answer = 99999999
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if(row[j] == 2):
            chickens.append([i, j])
        if(row[j] == 1):
            houses.append([i, j])


# 집마다 각 치킨 집 거리를 계산한다.
def calc(choices):
    global answer
    total = []
    for house in houses:
        sumD = []
        for c in choices:
            sumD.append(abs(house[0]-c[0]) + abs(house[1]-c[1]))
        total.append(min(sumD))

    answer = min(answer, sum(total))


# 치킨집을 m개 고르는 모든 경우의 수에 대해 계산
for p in combinations(chickens, m):
    calc(p)


print(answer)
