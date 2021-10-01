# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    queue = deque(people)
    # 무거운 사람을 태운 다음, 만약 자리가 비어있고, 가장 가벼운 사람의 무게를 더해도 limit보다 작으면 태운다.
    while(queue):
        count = 1
        weight = 0
        person = queue.popleft()
        weight += person
        while(count < 2 and queue and weight+queue[-1] <= limit):
            weight += queue.pop()
            count += 1
        answer += 1

    return answer


# solution([70, 50, 80, 50]	, 100)
