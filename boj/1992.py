# 출처 : https://www.acmicpc.net/problem/1992

# 범위 내의 값이 모두 같은지 체크하는 함수
def checkSame(x, y, n):
    value = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(value != graph[i][j]):
                return -1

    return value


# 재귀함수
def divide(x, y, n):
    global answer
    result = checkSame(x, y, n)
    # 범위내의 값이 같으면 해당값을 정답 문자열에 추가한다.
    if(result >= 0):
        answer += str(result)
    # 범위내의 값이 같지 않다면 4등분해서 재귀
    else:
        m = n//2
        answer += '('
        for i in range(2):
            for j in range(2):
                divide(x+i*m, y+j*m, m)
        answer += ')'


n = int(input())
graph = []
global answer
answer = ''
for i in range(n):
    graph.append(list(map(int, list(input()))))

divide(0, 0, n)
print(answer)
