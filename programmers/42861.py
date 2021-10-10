# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    # 코스트 정렬
    costs.sort(key=lambda x: (x[2]))
    # 현재 접근 가능한 섬번호 저장하는 possible
    possible = [costs[0][0], costs[0][1]]

    answer = costs[0][2]

    # 모든 섬을 갈 수 있을 때까지 반복
    while(len(possible) != n):
        # costs들을 돌면서 현재 갈 수 있고, 아직 가지 못한 섬의 비용을 증가시켜준다.
        for i in range(0, len(costs)):
            if(costs[i][0] in possible and costs[i][1] not in possible):
                possible.append(costs[i][1])
                answer += costs[i][2]
                break
            if(costs[i][1] in possible and costs[i][0] not in possible):
                possible.append(costs[i][0])
                answer += costs[i][2]
                break
    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]	)
