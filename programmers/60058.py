# 출처 : https://programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    answer = ''

    answer += split(p)
    return answer


def isBalance(elements):
    openCount = elements.count('(')
    closeCount = elements.count(')')

    if(openCount == closeCount):
        return True
    else:
        return False


def isRight(element):
    stack = []
    for el in element:
        if(el == '('):
            stack.append(el)
        else:
            if(len(stack) == 0):

                return False
            stack.pop()
    return True


def split(p):
    if(p == ''):
        return ''
    arr = list(p)
    stack = []
    elementList = []
    closeList = []
    u = ''
    v = ''
    while(True):
        elementList.append(arr.pop(0))

        if(isBalance(elementList)):
            u = ''.join(elementList)
            v = ''.join(arr)
            break

    if(isRight(u)):
        return u + split(v)
    else:
        recur_v = split(v)
        u = list(u)
        u.pop(0)
        u.pop()
        uReverse = []
        for i in u:
            if(i == '('):
                uReverse.append(')')
            else:
                uReverse.append('(')
        return '('+recur_v + ')'+''.join(uReverse)


solution("()))((()"	)
