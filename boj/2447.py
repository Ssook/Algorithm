# 출처 : https://www.acmicpc.net/problem/2447
# 공백으로 초기화
n = int(input())
graph = []
for i in range(n):
    row = [' ']*n
    graph.append(row)


# 재귀함수
def draw(x, y, n):
    # 사이즈가 3짜리면 *출력
    if(n == 3):
        for i in range(3):
            for j in range(3):
                if(i != 1 or j != 1):
                    graph[x+i][y+j] = '*'
    # 사이즈가 3이 아니라면 3으로 줄임
    else:
        m = n//3
        for i in range(3):
            for j in range(3):
                if(i != 1 or j != 1):
                    draw(x+i*m, y+j*m, m)


draw(0, 0, n)
for g in graph:
    print(''.join(g))
