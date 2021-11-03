# 출처 : https://www.acmicpc.net/problem/14888
import copy
n = int(input())
numbers = list(map(int, input().split()))
signs = list(map(int, input().split()))
answer = []


def recur(result, index, sign):

    if(index == n):
        answer.append(result)
        return
    if(sign[0] > 0):
        copySign = copy.deepcopy(sign)
        copySign[0] -= 1
        copyResult = result
        copyResult += numbers[index]
        recur(copyResult, index+1, copySign)
    if(sign[1] > 0):
        copySign = copy.deepcopy(sign)
        copySign[1] -= 1
        copyResult = result
        copyResult -= numbers[index]
        recur(copyResult, index+1, copySign)
    if(sign[2] > 0):
        copySign = copy.deepcopy(sign)
        copySign[2] -= 1
        copyResult = result
        copyResult *= numbers[index]
        recur(copyResult, index+1, copySign)
    if(sign[3] > 0):
        copySign = copy.deepcopy(sign)
        copySign[3] -= 1
        copyResult = result
        if(copyResult > 0):
            copyResult = copyResult // numbers[index]
        else:
            copyResult = copyResult*-1
            copyResult = (copyResult//numbers[index])*-1
        recur(copyResult, index+1, copySign)


recur(numbers[0], 1, signs)
print(max(answer))
print(min(answer))
