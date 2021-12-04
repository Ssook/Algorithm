# 출처 : https://www.acmicpc.net/problem/14503
n, m = map(int, input().split())
r, c, d = map(int, input().split())
# 각 방향에서 왼쪽 볼 때 d값을 딕셔너리로 관리
direction = {
    0: 3,
    1: 0,
    2: 1,
    3: 2,
}
#        북-서      동-북    남-동    서-남
moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]
graph = [list(map(int, input().split())) for _ in range(n)]

flag = True
isFull = [0, 0, 0, 0]
while(flag):
    # 1. 현재 위치를 청소한다.
    graph[r][c] = 2
    # 4방향 모두 청소할 곳이 없는지 체크하는 리스트
    isFull = [0, 0, 0, 0]
    # 2단계
    while(True):
        # 2.a 왼쪽방향 탐색
        nR = r+moves[d][0]
        nC = c+moves[d][1]
        # 왼쪽에 청소할 곳이 있는 경우
        if(nR >= 0 and nR < n and nC >= 0 and nC < m and graph[nR][nC] == 0):
            r = nR
            c = nC
            d = direction[d]
            isFull = [0, 0, 0, 0]
            break
        # 왼쪽방향에 청소할 공간이 없는 경우
        else:
            isFull[direction[d]] = 1  # 해당 방향에 청소할 곳이 없다고 체크
            # 네 방향 다 청소,벽인 경우
            if (isFull.count(1) == 4):
                d = direction[d]  # 후진을 위해 처음 방향으로 돌아옴
                # 후진하는 경우
                isFull = [0, 0, 0, 0]
                r = r-moves[(d+1) % 4][0]
                c = c-moves[(d+1) % 4][1]
                # 후진했는데 벽인 경우
                if(r > 0 and r < n and c > 0 and c < m and graph[r][c] == 1):
                    flag = False
                    break
                # 후진한 위치가 인덱스에서 벗어날 경우
                elif(r < 0 or r >= n or c < 0 or c >= m):
                    flag = False
                    break
            # 아직 네 방향 다 청소하지 않거나 체크하지 않은 경우 왼쪽방향으로 회전
            else:
                d = direction[d]
                continue

answer = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 2):
            answer += 1


print(answer)
