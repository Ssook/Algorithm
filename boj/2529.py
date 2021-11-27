# 출처 : https://www.acmicpc.net/problem/2529
from itertools import permutations
n = int(input())
signs = input('').split()
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

maxV = '0'
minV = '9999999999'


# 부등호를 만족하는지 체크하는 함수
def check(numberStr):
    numberStr = list(numberStr)

    for i in range(len(signs)):
        if(signs[i] == '>' and int(numberStr[i]) < int(numberStr[i+1])):
            return False
        elif(signs[i] == '<' and int(numberStr[i]) > int(numberStr[i+1])):
            return False

    return numberStr


# 모든 순열을 구해서 반복
for p in permutations(numbers, n+1):
    flag = check(p)
    if(flag != False):
        value = ''.join(flag)
        if(value > maxV):
            maxV = value
        if(value < minV):
            minV = value

print(maxV)
print(minV)
