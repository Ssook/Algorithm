# 출처 : https://www.acmicpc.net/problem/9663
n = int(input())
checkCol = [False for i in range(n)]
# 왼쪽위에서 오른쪽아래로 향하는 대각선
checkLu = [False for i in range(n+n)]
# 오른쪽위에서 왼쪽아래로 향하는 대각선
checkRu = [False for i in range(n+n)]


# 놓을 수 있는지 없는 지 판단하는 함수
def check(row, col):
    if(not checkCol[col] and not checkLu[abs(row-col+n-1)] and not checkRu[row+col]):
        return True
    else:
        return False


global answer
answer = 0


# 백트래킹 방식
# 한행씩 증가하면서 해당 행의 모든 열에 대해 반복문 수행
# 체크 함수를 통해 현재 행, 현재 열에 놓을 수 있다면, checkCol,Ru,Lu에 놓았다고 체크하고 다음 재귀 진행한 후, 값을 원래대로 돌려 놓음
def solution(row):
    global answer
    if(row == n):
        answer += 1
        return
    for i in range(n):
        if(check(row, i)):
            checkCol[i] = True
            checkRu[row+i] = True
            checkLu[abs(row-i+n-1)] = True
            solution(row+1)
            checkCol[i] = False
            checkRu[row+i] = False
            checkLu[abs(row-i+n-1)] = False


solution(0)
print(answer)
