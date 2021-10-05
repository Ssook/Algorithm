# 출처 : https://www.acmicpc.net/problem/1780

import sys
sys.setrecursionlimit(10000)

# x,y부터 n개의 칸이 모두 같은 값인지 체크


def checkSame(x, y, n):
    global graph
    value = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(graph[i][j] != value):
                return 99
    return value


# 재귀 함수
def divide(x, y, n):
    # 모두 같은 값이면 answer 리스트에 해당 값 추가
    result = checkSame(x, y, n)
    if(result != 99):
        answer.append(result)

    # 같지 않다면 9개의 구역을 나누어 재귀
    else:
        m = n//3
        for i in range(3):
            for j in range(3):
                divide(x+m*i, y+m*j, m)


answer = []

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

divide(0, 0, n)

print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))
