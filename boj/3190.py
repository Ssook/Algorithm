# 출처 : https://www.acmicpc.net/problem/3190
from collections import deque
n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
body = deque([[1, 1]])
moves = {}
for i in range(l):
    x, c = input().split()
    x = int(x)
    moves[x] = c

# 방향 바꾸는 함수


def changeDirection(nowDirection, c):
    if(c == 'D'):
        if(nowDirection == [-1, 0]):
            return [0, 1]
        elif(nowDirection == [1, 0]):
            return [0, -1]
        elif(nowDirection == [0, 1]):
            return [1, 0]
        elif(nowDirection == [0, -1]):
            return [-1, 0]
    if(c == 'L'):
        if(nowDirection == [-1, 0]):
            return [0, -1]
        elif(nowDirection == [1, 0]):
            return [0, 1]
        elif(nowDirection == [0, 1]):
            return [-1, 0]
        elif(nowDirection == [0, -1]):
            return [1, 0]


# print(moves)
direction = [0, 1]
time = 0
while(1):
    headX, headY = body[0]

    # 현재 머리가 벗어난 경우
    if(headX < 1 or headX > n or headY < 1 or headY > n):
        break

    # 다음 턴에 머리가 몸에 닿는 경우는 time을 1더하고 종료
    if([headX+direction[0], headY+direction[1]] in body):
        time += 1
        break

    # 다음 칸에 사과가 있는 경우
    if ([headX+direction[0], headY+direction[1]] in apples):
        apples.remove([headX+direction[0], headY+direction[1]])
        body.insert(0, [headX+direction[0], headY+direction[1]])
    else:
        body.pop()
        body.insert(0, [headX+direction[0], headY+direction[1]])

    time += 1
    
    # 방향 변경
    if(time in moves):
        direction = changeDirection(direction, moves[time])


print(time)
