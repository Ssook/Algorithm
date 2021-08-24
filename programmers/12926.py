# 출처 : https: // programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abcDict = {}
    noDict = {}
    for index, character in enumerate(list(abc)):
        noDict[index] = character
        abcDict[character] = index
    answer = ''
    strArr = list(s)

    for char in strArr:
        if(char == ' '):
            answer += ' '
        else:
            originNo = abcDict[char.lower()]
            if(ord(char) < 97):  # 대문자라면
                answer += noDict[(originNo+n) % 26].upper()
            else:
                answer += noDict[(originNo+n) % 26].lower()
    return answer


solution("AB", 1)
