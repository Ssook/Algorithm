# 출처 : https://www.acmicpc.net/problem/10971
from itertools import permutations
import sys
# 그래프 생성
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 9999999

l = range(0, n)
# 순열 완전 탐색
for case in permutations(l):
    sum = 0
    flag = False
    # 순열하나의 순서대로 순회하면서 비용 계산
    for i in range(len(case)-1):
        if(graph[case[i]][case[i+1]] != 0):
            sum += graph[case[i]][case[i+1]]
        else:
            flag = True
            break
    # 경로가 다 있고, 출발점으로 돌아오는 길도 있는 경우
    if(not flag and graph[case[n-1]][case[0]] != 0):
        sum += graph[case[-1]][case[0]]
        answer = min(answer, sum)

print(answer)
