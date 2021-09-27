# 출처 : https://programmers.co.kr/learn/courses/30/lessons/12985
import math


def solution(n, a, b):
    answer = 1
    minNo = min(a, b)
    maxNo = max(a, b)

    # 두 숫자가 1차이나고, 나누기 2한 값의 올림이 같을 때까지 반복
    while(True):
        if(maxNo-1 == minNo and ((math.ceil(maxNo/2)) == (math.ceil(minNo/2)))):
            break
        maxNo = math.ceil(maxNo/2)
        minNo = math.ceil(minNo/2)
        answer += 1
    return answer


solution(8, 2, 3)
