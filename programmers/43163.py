# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque


def solution(begin, target, words):
    global answer
    answer = []

    # 찾는 단어가 words에 없을 때
    if(target not in words):
        return 0

    # 시작 단어도 words에 넣어서 그래프 만들거임
    words.insert(0, begin)
    graph = []
    for i in range(len(words)):
        line = list(0 for i in range(len(words)))
        graph.append(line)

    for i in range(len(words)):
        for j in range(len(words)):
            count = 0
            for k in range(len(words[i])):
                if(words[i][k] != words[j][k]):
                    count += 1

            # 하나만 다르면 간선을 만들어 줘야함
            if(count == 1):
                graph[i][j] = 1

    # 방문한 기록 남기는 리스트
    visit = [0 for i in range(len(graph))]

    # dfs 수행

    def dfs(startNode, visit, target, words, count):
        count += 1
        if(visit[startNode] == 1):
            return

        # 찾는 단어면 정답에 여태온 count를 추가
        if(words[startNode] == target):
            return answer.append(count)

        # 방문 처리
        visit[startNode] = 1

        # 현재 노드에서 갈수 있는 노드들 찾아서 재귀
        for i in range(len(graph)):
            if(graph[startNode][i] == 1):
                dfs(i, visit, target, words, count)

    # 0번 노드에서 갈 수 있는 모든 노드들에 dfs 수행
    for i in range(len(graph)):
        if(graph[0][i]) == 1:
            count = 0
            (dfs(i, visit, target, words, count))

    return min(answer)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	)
