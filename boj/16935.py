# 출처 : https://www.acmicpc.net/problem/16935
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

commands = list(map(int, input().split()))


def no1(origin):
    newGraph = []
    for i in range(len(origin)-1, -1, -1):
        newGraph.append(origin[i])
    return newGraph


def no2(origin):
    newGraph = []
    for i in range(len(origin)):

        newGraph.append(list(reversed(origin[i])))

    return newGraph


def no3(origin):
    newGraph = []
    for col in range(len(origin[0])):
        target = []
        for row in range(len(origin)-1, -1, -1):
            target.append(origin[row][col])
        newGraph.append(target)

    return newGraph


def no4(origin):
    newGraph = []
    for col in range(len(origin[0])-1, -1, -1):
        target = []
        for row in range(len(origin)):
            target.append(origin[row][col])
        newGraph.append(target)

    return newGraph


def no5(origin):
    newGraph = [[0 for i in range(len(origin[0]))] for j in range(len(origin))]
    for i in range(len(origin)//2):
        for j in range(len(origin[0])//2):
            newGraph[i][j+len(origin[0])//2] = origin[i][j]

    for i in range(len(origin)//2):
        for j in range(len(origin[0])//2, len(origin[0])):
            newGraph[i+len(origin)//2][j] = origin[i][j]

    for i in range(len(origin)//2, len(origin)):
        for j in range(len(origin[0])//2, len(origin[0])):
            newGraph[i][j-len(origin[0])//2] = origin[i][j]

    for i in range(len(origin)//2, len(origin)):
        for j in range(len(origin[0])//2):
            newGraph[i-len(origin)//2][j] = origin[i][j]

    return newGraph


def no6(origin):
    newGraph = [[0 for i in range(len(origin[0]))] for j in range(len(origin))]
    for i in range(len(origin)//2):
        for j in range(len(origin[0])//2):
            newGraph[i+len(origin)//2][j] = origin[i][j]

    for i in range(len(origin)//2):
        for j in range(len(origin[0])//2, len(origin[0])):
            newGraph[i][j-len(origin[0])//2] = origin[i][j]

    for i in range(len(origin)//2, len(origin)):
        for j in range(len(origin[0])//2, len(origin[0])):
            newGraph[i-len(origin)//2][j] = origin[i][j]

    for i in range(len(origin)//2, len(origin)):
        for j in range(len(origin[0])//2):
            newGraph[i][j+len(origin[0])//2] = origin[i][j]

    return newGraph


# no2(graph)


for c in commands:
    if(c == 1):
        graph = no1(graph)
    if(c == 2):
        graph = no2(graph)
    if(c == 3):
        graph = no3(graph)
    if(c == 4):
        graph = no4(graph)
    if(c == 5):
        graph = no5(graph)
    if(c == 6):
        graph = no6(graph)

for row in graph:
    for col in range(len(row)):
        print(row[col], end=' ')
    print('')
