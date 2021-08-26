# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = []
    stack = []
    count = 0

    for i in range(len(prices)):
        nowPrice = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            if(prices[j] >= nowPrice):
                count += 1
            else:
                count += 1
                answer.append(count)
                count = 0
                break
        if(count > 0):
            answer.append(count)

    answer.append(0)
    return answer
