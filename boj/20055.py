# 출처 : https://www.acmicpc.net/problem/20055
# (1) 로봇이 있는 인덱스를 리스트로 관리해서 풀이 실패
# time = 1
# while(1):
#     print('-------')
#     print(numbers)
#     print(robots)
#     # 1.
#     numbers.rotate(1)
#     nRobots = []
#     for i in range(len(robots)):
#         robots[i] += 1
#         if(robots[i] != n-1):
#             nRobots.append(robots[i])
#     robots = nRobots
#     print(numbers)
#     print(robots)
#     # 2.
#     if(robots):
#         nRobots = []
#         for i in range(len(robots)):
#             if(robots[i]+1 not in robots and numbers[robots[i]+1] > 0):
#                 numbers[robots[i]+1] -= 1
#                 if(robots[i]+1 != n-1):
#                     nRobots.append(robots[i]+1)
#         robots = nRobots
#     # 3.
#     if(numbers[0] > 0):
#         robots.append(0)
#         numbers[0] -= 1

#     # 4.
#     if(numbers.count(0) >= k):
#         break

#     time += 1

# print(numbers)
# print(robots)

# print(time)

# 리스트로 자리 다 만들어 놓고 0,1로 풀이
from collections import deque
n, k = map(int, input().split())
numbers = deque(list(map(int, input().split())))
robots = deque([0 for _ in range(2*n)])
time = 1

while(True):
    # 1단계 수행
    numbers.rotate(1)
    robots.rotate(1)
    # 내리는 경우
    robots[n-1] = 0

    # 2단계 수행
    for i in range(n-2, -1, -1):
        if(robots[i] == 1 and robots[i+1] == 0 and numbers[i+1] > 0):
            robots[i] = 0
            robots[i+1] = 1
            numbers[i+1] -= 1
    robots[n-1] = 0

    # 3단계
    if(numbers[0] > 0):
        robots[0] = 1
        numbers[0] -= 1

    # 4단계
    if(numbers.count(0) >= k):
        break

    time += 1

print(time)
