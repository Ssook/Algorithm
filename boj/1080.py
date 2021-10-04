# 선택한 좌표부터 3x3 영역을 뒤집어서 반환하는 함수
def reverseMatrix(matrix, row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
            if(matrix[i][j]) == '0':
                matrix[i][j] = '1'
            else:
                matrix[i][j] = '0'
    return matrix


n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(input()))

for i in range(n):
    b.append(list(input()))


answer = 0
# 3x3구간에서 왼쪽위의 꼭지점만 보고 뒤집을지 말지 판별한다.
for i in range(0, n-2):
    for j in range(0, m-2):
        # print(b[i][j] != a[i][j])
        if(b[i][j] != a[i][j]):
            a = reverseMatrix(a, i, j)
            answer += 1


# 다 바꾸고 나서도 값이 다른지, 즉 a로 b를 만들어내는 것이 불가능한지 판별
isComplete = True
for i in range(n):
    for j in range(m):
        if(a[i][j] != b[i][j]):
            isComplete = False
            break

if(isComplete):
    print(answer)
else:
    print(-1)
