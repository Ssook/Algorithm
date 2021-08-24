# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = {}
    answer = 0
    for arr in clothes:
        key = arr[1]
        if(key in dic):
            dic[key] = dic[key]+1
        else:
            dic[key] = 1

    count = 1
    for item in dic.items():
        count = count * (item[1]+1)

    answer = count-1

    return answer


solution([["yellowhat", "headgear"], ["bluesunglasses",
         "eyewear"], ["green_turban", "headgear"]]	)
