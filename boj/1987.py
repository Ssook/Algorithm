# 출처 : https://www.acmicpc.net/problem/1987
# 그래프 그리기
r, c = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(input()))

global answer
answer = 0
# 상하좌우
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# dfs사용해서 탐색


def dfs(x, y, roads):
    global answer
    # 현재 알파벳 추가
    roads += graph[x][y]
    # 상하좌우 다 못가는 것을 체크하기 위한 변수
    flag = True
    # 상하좌우 보고 아직 안갔으면 방문
    for move in moves:
        if(x+move[0] >= 0 and x+move[0] < r and y+move[1] >= 0 and y+move[1] < c):
            if(graph[x+move[0]][y+move[1]] not in roads):
                dfs(x+move[0], y+move[1], roads)
                flag = False
    # flag==True라면 탐색 종료
    if(flag):
        answer = max(answer, len(roads))


dfs(0, 0, '')
print(answer)
