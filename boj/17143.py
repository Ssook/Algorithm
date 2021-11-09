# 출처 : https://www.acmicpc.net/problem/17143
r, c, m = map(int, input().split())
graph = [[0 for i in range(c)] for j in range(r)]
fish = {}
for i in range(m):
    row, col, s, d, z = map(int, input().split())
    fish[str(i)] = (row-1, col-1, s, d, z)

answer = 0


# 낚시왕 이동
for col in range(c):
    # 상어 풀기
    deleteTargetKey = []  # 같은 위치에 있어서 잡아먹히는 상어의 키 저장
    for key in fish:
        rowF, colF, s, d, z = fish[key]
        # 잡아 먹히는 경우
        if(graph[rowF][colF] != 0):
            vsFish = graph[rowF][colF]
            if(vsFish[2] < z):
                deleteTargetKey.append(vsFish[3])
                graph[rowF][colF] = (s, d, z, key)
            else:
                deleteTargetKey.append(key)
        else:
            graph[rowF][colF] = (s, d, z, key)

    # 딕셔너리에서 잡아먹힌 상어 삭제
    for target in deleteTargetKey:
        del fish[target]

    # 가장 가까운 상어 잡음
    for row in range(r):
        if(graph[row][col] != 0):
            answer += graph[row][col][2]
            del fish[graph[row][col][3]]
            break

    # 상어 이동
    graph = [[0 for i in range(c)] for j in range(r)]
    for key in fish:
        row, col, originSpeed, direction, fishSize = fish[key]
        speed = originSpeed

        while(speed > 0):
            if(direction == 1):
                if(row > 0):
                    speed -= 1
                    row -= 1
                if(row == 0):
                    direction = 2
            elif(direction == 2):
                if(row < r-1):
                    speed -= 1
                    row += 1
                if(row == r-1):
                    direction = 1
            elif(direction == 3):
                if(col < c-1):
                    col += 1
                    speed -= 1
                if(col == c-1):
                    direction = 4
            elif(direction == 4):
                if(col > 0):
                    col -= 1
                    speed -= 1
                if(col == 0):
                    direction = 3

        fish[key] = (row, col, originSpeed, direction, fishSize)

print(answer)
