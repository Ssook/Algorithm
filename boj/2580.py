# 출처 : https://www.acmicpc.net/problem/2580
checkRow = [[0 for i in range(10)] for j in range(9)]
checkCol = [[0 for i in range(10)] for j in range(9)]
checkBox = [[0 for i in range(10)] for j in range(9)]

graph = []
for i in range(9):
    graph.append(list(map(int, input().split())))


def box(i, j):
    return (3 * (i//3))+j//3


# 그래프 그리기
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if(graph[i][j] != 0):
            checkRow[i][graph[i][j]] = 1
            checkCol[j][graph[i][j]] = 1
            checkBox[box(i, j)][graph[i][j]] = 1

# 숫자가 들어갈 수 있는 지 체크하는 함수


def check(row, col, no):
    if(checkCol[col][no] == 0 and checkRow[row][no] == 0 and checkBox[box(row, col)][no] == 0):
        return True
    else:
        return False


def sdoku(z):
    if(z == 81):
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                print(graph[i][j], end=' ')
            print('')
        exit()
    x = (z//9)
    y = (z % 9)

    if(graph[x][y] != 0):
        sdoku(z+1)
    else:
        # 백트래킹
        for i in range(1, 10):
            if(check(x, y, i)):
                graph[x][y] = i
                checkCol[y][i] = 1
                checkRow[x][i] = 1
                checkBox[(box(x, y))][i] = 1
                sdoku(z+1)
                graph[x][y] = 0
                checkCol[y][i] = 0
                checkRow[x][i] = 0
                checkBox[(box(x, y))][i] = 0


sdoku(0)
