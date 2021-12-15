# 출처 : https://www.acmicpc.net/problem/18428
from itertools import combinations


# 각 선생님 좌표를 받아서 학생을 찾을 수 있는지 확인하는 함수
def find(x, y):
    # 상
    for i in range(x-1, -1, -1):
        if(graph[i][y] == 'S'):
            return True
        elif(graph[i][y] == 'O'):
            break
    # 하
    for i in range(x+1, n):
        if(graph[i][y] == 'S'):
            return True
        elif(graph[i][y] == 'O'):
            break
    # 좌
    for i in range(y-1, -1, -1):
        if(graph[x][i] == 'S'):
            return True
        elif(graph[x][i] == 'O'):
            break
    # 우
    for i in range(y+1, n):
        if(graph[x][i] == 'S'):
            return True
        elif(graph[x][i] == 'O'):
            break

    return False


n = int(input())
graph = [input().split() for _ in range(n)]

teachers = []
blanks = []


# 현재 벽 배열로 모든 학생이 피할 수 있는지 확인하는 함수
def check():
    for t in teachers:
        if find(t[0], t[1]):
            return True
    return False


for i in range(n):
    for j in range(n):
        if(graph[i][j] == 'X'):
            # 빈 공간들 추가
            blanks.append([i, j])
        elif(graph[i][j] == 'T'):
            # 선생님 위치 추가
            teachers.append([i, j])

# 빈 공간들에서 3개 선택하는 조합
for c in combinations(blanks, 3):
    # 장애물 설치
    for l in c:
        graph[l[0]][l[1]] = 'O'

    # 현재 배열로 선생님들이 학생들 못 찾으면 출력하고 종료
    if not check():
        print('YES')
        exit(0)

    # 장애물 다시 뺌
    for l in c:
        graph[l[0]][l[1]] = 'X'
print('NO')


# 재귀 함수로 장애물 설치하는 코드 실패
# n = int(input())
# graph = [input().split() for _ in range(n)]
# teachers = []
# for i in range(n):
#     for j in range(n):
#         if(graph[i][j] == 'T'):
#             teachers.append([i, j])


# def find(x, y):
#     # 상
#     for i in range(x-1, -1, -1):
#         if(graph[i][y] == 'S'):
#             return True
#         elif(graph[i][y] == 'O'):
#             break
#     # 하
#     for i in range(x+1, n):
#         if(graph[i][y] == 'S'):
#             return True
#         elif(graph[i][y] == 'O'):
#             break
#     # 좌
#     for i in range(y-1, -1, -1):
#         if(graph[x][i] == 'S'):
#             return True
#         elif(graph[x][i] == 'O'):
#             break
#     # 우
#     for i in range(y+1, n):
#         if(graph[x][i] == 'S'):
#             return True
#         elif(graph[x][i] == 'O'):
#             break

#     return False


# def check():
#     # for i in range(n):
#     #     for j in range(n):
#     #         if(graph[i][j] == 'T'):
#     for t in teachers:
#         if (find(t[0], t[1])):
#             return True
#     return False


# def recur(count, number):
#     x = number//n
#     y = number % n
#     if(number == n**2):
#         return
#     if(count == 3):
#         if not check():
#             print('YES')
#             exit(0)

#     if(graph[x][y] == 'X'):
#         graph[x][y] = 'O'
#         recur(count+1, number+1)
#         graph[x][y] = 'X'
#         recur(count, number+1)
#     else:
#         recur(count, number+1)


# recur(0, 0)
# print('NO')
