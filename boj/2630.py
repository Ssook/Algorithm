# 출처 : https://www.acmicpc.net/problem/2630
# 값이 다 같은지 체크해주는 함수
def checkSame(square):
    value = square[0][0]
    for i in range(len(square)):
        for j in range(len(square)):
            if(square[i][j] != value):
                return -1
    return value

# 재귀함수


def divide(square):
    global answerZero, answerOne
    if(checkSame(square) == 0):
        answerZero += 1
    elif(checkSame(square) == 1):
        answerOne += 1
    # 값이 다 같지 않다면 4등분해서 재귀
    else:
        mid = len(square)//2
        graph = []
        for i in range(0, mid):
            graph.append(square[i][0:mid])
        divide(graph)
        graph = []
        for i in range(0, mid):
            graph.append(square[i][mid:len(square)])
        divide(graph)
        graph = []
        for i in range(mid, len(square)):
            graph.append(square[i][0:mid])
        divide(graph)
        graph = []
        for i in range(mid, len(square)):
            graph.append(square[i][mid:len(square)])
        divide(graph)


global answerZero
answerZero = 0
global answerOne
answerOne = 0
n = int(input())
square = []
for i in range(n):
    square.append(list(map(int, input().split())))

divide(square)

print(answerZero)
print(answerOne)
