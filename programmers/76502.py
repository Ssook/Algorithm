# 출처 : https://programmers.co.kr/learn/courses/30/lessons/76502

import copy


def checkStack(s):
    temp = copy.deepcopy(s)
    stack = []

    for string in temp:

        if(string == '}' or string == ']' or string == ')'):
            if(len(stack) == 0):
                return False
            else:
                topValue = stack.pop()
                if(not (ord(topValue) <= ord(string) and ord(string) <= ord(topValue)+2)):
                    return False
        else:
            stack.append(string)

    if(len(stack) == 0):
        return True
    else:
        return False


def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if i != 0:
            s.append(s.pop(0))

        if(checkStack(s)):
            answer += 1
    return answer


solution("[](){}")
