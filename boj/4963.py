# 출처 : https://www.acmicpc.net/problem/4963

def dfs(x, y):
    global graph
    dxList = [-1, 0, 1]
    dyList = [-1, 0, 1]
    graph[x][y] = 0
    for dx in dxList:
        for dy in dyList:
            if((x+dx >= 0 and x+dx < h) and (y+dy >= 0 and y+dy < w)):
                if(graph[x+dx][y+dy] == 1):
                    dfs(x+dx, y+dy)


while(True):
    answer = 0
    w, h = map(int, input().split())
    visit = [[0 for a in range(w)] for b in range(h)]

    if(w == 0 and h == 0):
        break
    global graph
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split(' '))))

    for x in range(h):
        for y in range(w):
            if(graph[x][y] == 1):
                answer += 1
                dfs(x, y)
    print(answer)
