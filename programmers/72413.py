from collections import deque
import heapq
INF = 99999999


def solution(n, s, a, b, fares):
    answer = []

    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    for f in fares:
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]

    # 다익스트라 함수
    def dijkstra(start):
        queue = [(0, start)]
        check = [0 for _ in range(n+1)]
        distance = [INF for _ in range(n+1)]
        distance[start] = 0

        while(queue):
            cost, cur = heapq.heappop(queue)
            if(check[cur] == 1):
                continue
            check[cur] = 1

            for i in range(1, n+1):
                if(graph[cur][i] > 0 and distance[i] >= cost+graph[cur][i] and check[i] == 0):
                    heapq.heappush(queue, (cost+graph[cur][i], i))
                    distance[i] = cost+graph[cur][i]

        return distance

    # 시작점에서 각 지점까지의 최소 비용 거리
    minFares = dijkstra(s)

    # 시작점에서 i번까지 갔다고 치고, i점에서 다익스트라 수행해서 집까지의 요금 계산
    for i in range(1, n+1):
        if(i != s):
            ll = dijkstra(i)
            answer.append(minFares[i]+ll[a]+ll[b])

    # 합승 안한게 더 낮은 경우가 있을 수 있음
    return min(minFares[a]+minFares[b], min(answer))
