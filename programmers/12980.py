# 출처 : https: // programmers.co.kr/learn/courses/30/lessons/12980


# bfs로 풀면 풀리기는 하지만 시간초과 발생
# from collections import deque

# def solution(n):
#     ans = 0

#     electricQ = deque([0])
#     visit = [0]
#     queue = deque([0])
#     while(queue):
#         # print(queue)
#         curLocation = queue.popleft()
#         electric = electricQ.popleft()
#         if(curLocation*2 == n):
#             # print(electric)
#             ans = electric
#             break
#         if(curLocation+1 == n):
#             ans = electric+1
#             break
#         if(curLocation*2 not in visit and curLocation*2 <= n):
#             visit.append(curLocation*2)
#             queue.append(curLocation*2)
#             electricQ.append(electric)
#         if(curLocation+1 not in visit and curLocation+1 <= n):
#             visit.append(curLocation+1)
#             queue.append(curLocation+1)
#             electricQ.append(electric+1)

#     return ans

# n이 짝수면 2배해서 0의 비용으로 갈 수 있다. 예를 들어 16이나 32나 64나 비용은 동일.
# n이 홀수면 비용이 1증가한다.


def solution(n):
    answer = 0
    while(n != 0):
        # print(n)
        if(n % 2 == 0):
            n = n//2
        else:
            n = n-1
            answer += 1
    print(answer)


solution(5)
