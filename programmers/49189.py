# 출처 : https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque


def solution(n, edge):
    # 그래프 그리기(시간복잡도 때문에 인접리스트 방식으로 구현해주어야 함)
    answer = []
    graph = {}
    for i in range(n):
        graph[i] = []

    for road in edge:
        graph[road[0]-1].append(road[1]-1)
        graph[road[1]-1].append(road[0]-1)

    visit = [0 for i in range(n)]
    queue = deque([0])
    visit[0] = 1
    count = 1
    # 몇 계층인지 알기 위한 딕셔너리
    layerDict = {
        0: 0
    }

    # bfs로 구현
    while(queue):
        curNode = queue.popleft()
        thisLayer = layerDict[curNode]+1
        for j in (graph[curNode]):
            if(visit[j] == 0):
                queue.append(j)
                layerDict[j] = thisLayer
                visit[j] = 1
        count += 1

    for key in layerDict:
        answer.append(layerDict[key])
    maxNo = answer[-1]

    return answer.count(maxNo)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)
