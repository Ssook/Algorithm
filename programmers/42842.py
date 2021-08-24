# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown+yellow

    for width in range(3, 5000):
        for height in range(3, width+1):

            if(width*height == total and (width-2) * (height-2) == yellow):
                answer = [width, height]

    return answer


solution(8, 1)
