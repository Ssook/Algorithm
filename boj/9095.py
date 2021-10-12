# # 출처 : https://www.acmicpc.net/problem/9095
# 풀이 1 : dp
# t = int(input())
# d = [0 for i in range(13)]
# d[1] = 1
# d[2] = 2
# d[3] = 4
# for i in range(4, 13):
#     d[i] = d[i-1]+d[i-2]+d[i-3]

# for k in range(t):

#     n = int(input())
#     print(d[n])

# 풀이 2 : 재귀 형태로 풀이
global answer
answer = 0


def solution(sum, goal):
    global answer
    if(sum > goal):
        return
    elif(sum == goal):
        answer += 1
    else:
        solution(sum+1, goal)
        solution(sum+2, goal)
        solution(sum+3, goal)


t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    solution(1, n)
    solution(2, n)
    solution(3, n)
    print(answer)
