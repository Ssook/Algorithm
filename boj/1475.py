# 출처 : https://www.acmicpc.net/problem/1475
number = list(input())
noDict = {}

for i in range(10):
    n = i
    if(i == 9):
        n = 6
    noDict[str(n)] = 0


# 모든 카드 추가
def newSet(noDict):
    for i in range(10):
        n = i
        if(i == 9):
            n = 6

        noDict[str(n)] += 1
    return noDict


answer = 0
for i in range(len(number)):
    no = number[i]
    if(no == '9'):
        no = '6'
    if(noDict[str(no)] == 0):
        noDict = newSet(noDict)
        answer += 1
    noDict[str(no)] -= 1

print(answer)
