# 출처 : https://www.acmicpc.net/problem/1799
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 흑백 나누어서 백트래킹
checkR = [0 for i in range(n*2)]
checkL = [0 for i in range(n*2)]
black = []
white = []
for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            if((i+j) % 2 == 0):
                black.append((i, j))
            else:
                white.append((i, j))


def check(i, j):
    if(checkR[i+j] == 1 or checkL[i-j+n-1] == 1):
        return False
    return True


oddAnswer = 0
evenAnswer = 0


def oddRecur(count, index):
    global oddAnswer
    oddAnswer = max(oddAnswer, count)
    if(index == len(black)):
        return
    i, j = black[index]
    if(check(i, j)):
        checkR[i+j] = 1
        checkL[i-j+n-1] = 1
        oddRecur(count+1, index+1)
        checkR[i+j] = 0
        checkL[i-j+n-1] = 0
        oddRecur(count, index+1)
    else:
        oddRecur(count, index+1)


def evenRecur(count, index):
    global evenAnswer
    evenAnswer = max(evenAnswer, count)
    if(index == len(white)):
        return
    i, j = white[index]
    if(check(i, j)):
        checkR[i+j] = 1
        checkL[i-j+n-1] = 1
        evenRecur(count+1, index+1)
        checkR[i+j] = 0
        checkL[i-j+n-1] = 0
        evenRecur(count, index+1)
    else:
        evenRecur(count, index+1)


answer = 0


oddRecur(0, 0)
evenRecur(0, 0)
print((oddAnswer)+(evenAnswer))
