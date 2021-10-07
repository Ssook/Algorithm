# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while(len(scoville) >= 2):
        # 제일 작은 값이 K보다 커지면 break
        if(scoville[0] >= K):
            break
        count += 1
        # 두 값을 빼서 다시 넣어준다
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)

    # 반복문을 거치고나서 첫번째 원소가 K보다 작으면 불가능한 경우이다.
    if(scoville[0] < K):
        return -1
    else:
        return count
