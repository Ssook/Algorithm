# 출처 : https://www.acmicpc.net/problem/4195
def find(x):
    if(parent[x] == x):
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    pX = find(x)
    pY = find(y)
    if(pX > pY):
        pX, pY = pY, pX
    if(pX != pY):
        parent[pY] = pX
        total[pX] += total[pY]
        total[pY] = 0
    print(total[pX])

# 이름을 숫자로 맵핑


def strToInt(name, nameDict, count):
    if(name in nameDict):
        return [nameDict[name], count]
    else:
        nameDict[name] = count
        count += 1
        return [nameDict[name], count]


t = int(input())
for _ in range(t):
    nameDict = {}
    count = 0
    n = int(input())
    parent = [i for i in range(200003)]
    total = [1 for i in range(200003)]
    for i in range(n):
        a, b = input().split()
        a, count = strToInt(a, nameDict, count)
        b, count = strToInt(b, nameDict, count)
        if(a > b):
            a, b = b, a

        union(a, b)
