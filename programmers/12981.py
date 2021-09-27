# 출처 : https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    dict = {}
    lastWord = ''

    for i in range(len(words)):

        if((words[i] in dict) or (lastWord != '' and lastWord != words[i][0])):
            answer.append((i % n)+1)
            answer.append((i//n)+1)
            break
        dict[words[i]] = (i) % n
        lastWord = words[i][-1]
    if(len(dict) == len(words)):
        answer = [0, 0]

    return answer
