# 출처 : https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq


def solution(N, road, K):
    INF = 100000000
    answer = 0
    graph = [[0 for i in range(N)] for j in range(N)]
    # 그래프 만드는 과정
    for r in road:
        if(r[2] < graph[r[0]-1][r[1]-1] or graph[r[0]-1][r[1]-1] == 0):
            graph[r[0]-1][r[1]-1] = r[2]
            graph[r[1]-1][r[0]-1] = r[2]

    # 시작 정점부터의 거리
    distance = [INF for i in range(N)]
    # 해당 정점이 처리되었는지 확인
    check = [0 for i in range(N)]

    start = 0
    distance[start] = 0
    queue = [(0, start)]

    # 다익스트라 수행
    while (queue):
        minDistance, nowIndex = heapq.heappop(queue)
        if(check[nowIndex] == 1):
            continue
        check[nowIndex] = 1
        for i in range(len(graph[nowIndex])):
            if(graph[nowIndex][i] != 0 and distance[nowIndex]+graph[nowIndex][i] < distance[i]):
                distance[i] = distance[nowIndex]+graph[nowIndex][i]
                heapq.heappush(
                    queue, (distance[nowIndex]+graph[nowIndex][i], i))

    for d in distance:
        if(d <= K):
            answer += 1

    return answer
