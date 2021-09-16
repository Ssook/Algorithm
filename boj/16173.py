n = int(input())
gameMap = []
global success
success = False

# 맵 만들기
for i in range(n):
    line = list(map(int, input().split()))
    gameMap.append(line)


def dfs(x, y):
    global success

    # 게임 맵 초과할 경우
    if(x >= n or y >= n):
        return
    # 자리에 써있는 숫자가 맵보다 크면 무조건 아웃, 0이면 목적지에 도착 불가능,
    if(gameMap[x][y] >= n or gameMap[x][y] == 0):
        return

    # 목적지에 도착한 경우
    if(gameMap[x][y] == -1):
        success = True
        return

    # 재귀적으로 dfs 수행
    dfs(x+gameMap[x][y], y)  # 오른쪽으로
    dfs(x, y+gameMap[x][y])  # 아래로


dfs(0, 0)

if(success):
    print('HaruHaru')
else:
    print('Hing')
