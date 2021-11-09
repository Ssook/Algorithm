# 출처 : https://www.acmicpc.net/problem/20040
n, m = map(int, input().split())

parent = [i for i in range(n)]
cmd = []


def find(x):
    if(x == parent[x]):
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    # 이 부분 안하면 메모리 초과 발생
    if(x < y):
        y, x = x, y
    parent[x] = y


# for i in range(m):
#     a, b = map(int, input().split())
#     cmd.append((a, b))

for i in range(m):
    a, b = map(int, input().split())

    pA = find(a)
    pB = find(b)
    # 둘이 같은 그룹에 속해있으면 싸이클 완성
    if(pA == pB):
        print(i+1)
        exit(0)
    # 아니면 둘을 유니온
    else:
        union(pA, pB)


print(0)
