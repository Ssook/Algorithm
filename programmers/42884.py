# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 0
    # 나가는 시점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    point = routes[0][1]
    answer += 1
    # 전에 설치한 점이 범위 안에 있으면 스킵하고 아니면 새로운 카메라를 설치하고 포인트를 지정
    for i in range(len(routes)):
        if(point in range(routes[i][0], routes[i][1]+1)):
            continue
        else:
            point = routes[i][1]
            answer += 1
    return answer
