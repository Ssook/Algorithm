n = int(input())
gameMap = []
global success
success = False
for i in range(n):
    line = list(map(int, input().split()))
    gameMap.append(line)


def dfs(x, y):
    global success
    if(x >= n or y >= n):
        return
    if(gameMap[x][y] >= n or gameMap[x][y] == 0):
        return

    if(gameMap[x][y] == -1):
        success = True
        return

    dfs(x+gameMap[x][y], y)  # 오른쪽으로
    dfs(x, y+gameMap[x][y])  # 아래로


dfs(0, 0)

if(success):
    print('HaruHaru')
else:
    print('Hing')
