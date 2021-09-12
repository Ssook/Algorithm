# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def solution(n, computers):
    global answer
    answer = 0
    visit = []
    for i in range(n):
        visit.append(False)

    def bfs(i):
        if(visit[i]):
            return

        global answer
        answer += 1
        queue = deque([i])

        while(queue):
            nowNode = queue.popleft()
            visit[nowNode] = True

            for i in range(n):
                if(computers[nowNode][i] == 1 and not visit[i]):
                    queue.append(i)

    for i in range(n):
        bfs(i)

    return answer
