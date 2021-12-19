# 출처 : https://www.acmicpc.net/problem/2798
from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = -1
for c in combinations(cards, 3):
    sum = c[0]+c[1]+c[2]
    if(sum > answer and sum <= m):
        answer = sum

print(answer)
