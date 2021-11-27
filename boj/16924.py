n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]


# x,y 좌표에서 size 크기의 십자가를 그리는 함수
def draw(board, x, y, size):
    if(x-size >= 0 and x+size < n and y-size >= 0 and y+size < m):
        for k in range(-size, size+1):
            board[x][y+k] = '*'
            board[x+k][y] = '*'

    return board

# board와 graph가 같은지 체크하는 함수


def checkSame(board):
    for i in range(n):
        for j in range(m):
            if(board[i][j] != graph[i][j]):
                return False
    return True

# x,y좌표로부터 십자가의 크기가 얼마나 되는지 체크 하는 함수


def checkSize(x, y):
    size = 0
    i = 1

    while(True):
        # i값을 하나씩 증가시키면서(십자가 길이) 십자가가 되는지 확인
        if(x-i >= 0 and x+i < n and y-i >= 0 and y+i < m):
            if (graph[x][y] == '*' and graph[x-i][y] == '*' and graph[x+i][y] == '*' and graph[x][y-i] == '*' and graph[x][y+i] == '*'):
                i += 1
            else:
                size = i-1
                break
        else:
            size = i-1
            break
    return size


cross = []


isAnswer = False
board = [['.' for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        # 현재 좌표가 *일 경우 십자가가 성립되는지 체크하고 사이즈를 구해 그린다.
        if(graph[i][j] == '*'):
            size = checkSize(i, j)
            if(size > 0):
                board = draw(board, i, j, size)
                cross.append([i+1, j+1, size])
                # 두 판이 같다면 정답 출력
                if(checkSame(board)):
                    isAnswer = True
                    print(len(cross))
                    for c in cross:
                        print(*c)


if(not isAnswer):
    print(-1)
